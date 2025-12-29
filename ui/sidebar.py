import streamlit as st

LANGUAGE_OPTIONS = {
    "English": "en-US",
    "Hindi": "hi-IN",
    "Spanish": "es-ES",
    "French": "fr-FR",
    "German": "de-DE",
}


def render_sidebar():
    st.sidebar.title("🌐 LexiSync Settings")

    input_langs = st.sidebar.multiselect(
        "Spoken Languages (Input)",
        options=list(LANGUAGE_OPTIONS.keys()),
        default=["English"],
    )

    output_lang = st.sidebar.selectbox(
        "Output Language",
        options=list(LANGUAGE_OPTIONS.keys()),
        index=0,
    )

    st.session_state.selected_input_languages = [
        LANGUAGE_OPTIONS[l] for l in input_langs
    ]
    st.session_state.selected_output_language = LANGUAGE_OPTIONS[output_lang][:2]

    st.sidebar.markdown("---")
    st.sidebar.info("Real-time multilingual meeting assistant")

