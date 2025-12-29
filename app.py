import streamlit as st
import threading
import time

# --- UI ---
from ui.state import init_state
from ui.sidebar import render_sidebar
from ui.meeting_controls import render_meeting_controls
from ui.live_subtitles import render_live_subtitles
from ui.knowledge_map import render_knowledge_map
from ui.summary_view import render_summary_view

# --- Speech Engine ---
from speech_engine.live_stream import LiveSpeechEngine

# --- Reasoning & Memory ---
from reasoning_engine.gemini_client import GeminiReasoningEngine
from memory.store import MemoryStore

# --- Utils ---
from utils.logger import get_logger
from utils.text_utils import clean_transcript, is_meaningful
from utils.time_utils import utc_now

logger = get_logger(__name__)

st.set_page_config(
    page_title="LexiSync – Multilingual Meeting AI",
    layout="wide",
)

# ---------- INIT ----------
init_state()
render_sidebar()

st.title("🎧 LexiSync – Real-Time Multilingual Meeting Assistant")

render_meeting_controls()

# ---------- GLOBAL OBJECTS ----------
if "speech_engine" not in st.session_state:
    st.session_state.speech_engine = None

if "reasoning_engine" not in st.session_state:
    st.session_state.reasoning_engine = GeminiReasoningEngine()

if "memory_store" not in st.session_state:
    st.session_state.memory_store = MemoryStore()

# ---------- SPEECH THREAD ----------
def speech_loop():
    engine = LiveSpeechEngine(
        input_languages=st.session_state.selected_input_languages,
        output_language=st.session_state.selected_output_language,
    )

    st.session_state.speech_engine = engine
    responses = engine.start()

    for data in engine.process_responses(responses):
        if not st.session_state.meeting_running:
            break

        original = clean_transcript(data["original"])
        translated = clean_transcript(data["translated"])

        if not is_meaningful(original):
            continue

        st.session_state.live_transcript.append(original)
        st.session_state.translated_transcript.append(translated)

        # Store memory
        st.session_state.memory_store.store_turn(
            text=original,
            translated=translated,
            timestamp=utc_now(),
        )

        time.sleep(0.01)

    engine.stop()
    logger.info("Speech engine stopped")


# ---------- START / STOP HANDLING ----------
if st.session_state.meeting_running and st.session_state.speech_engine is None:
    logger.info("Starting speech thread")
    threading.Thread(target=speech_loop, daemon=True).start()

if not st.session_state.meeting_running and st.session_state.live_transcript:
    logger.info("Running reasoning engine")

    summary = st.session_state.reasoning_engine.generate_summary(
        st.session_state.memory_store.get_full_transcript()
    )

    st.session_state.meeting_summary = summary

# ---------- UI LAYOUT ----------
col1, col2 = st.columns([2, 1])

with col1:
    render_live_subtitles()
    render_summary_view()

with col2:
    render_knowledge_map()

st.markdown("---")
st.caption("© 2025 LexiSync | Real-time multilingual meeting intelligence")
