import streamlit as st


def render_live_subtitles():
    st.subheader("🗣 Live Subtitles")

    transcript_box = st.container(height=300)

    with transcript_box:
        for original, translated in zip(
            st.session_state.live_transcript,
            st.session_state.translated_transcript,
        ):
            st.markdown(f"**🟦 {original}**")
            st.markdown(f"🟩 _{translated}_")
            st.markdown("---")
