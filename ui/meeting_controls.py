import streamlit as st


def render_meeting_controls():
    col1, col2 = st.columns(2)

    with col1:
        if not st.session_state.meeting_running:
            if st.button("▶️ Start Meeting Bot", use_container_width=True):
                st.session_state.meeting_running = True

    with col2:
        if st.session_state.meeting_running:
            if st.button("⏹ Stop Meeting", use_container_width=True):
                st.session_state.meeting_running = False
