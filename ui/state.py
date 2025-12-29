import streamlit as st


def init_state():
    defaults = {
        "meeting_running": False,
        "live_transcript": [],
        "translated_transcript": [],
        "knowledge_items": [],
        "selected_input_languages": ["en-US"],
        "selected_output_language": "en",
        "meeting_summary": "",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
