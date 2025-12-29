import streamlit as st


def render_summary_view():
    st.subheader("📌 Meeting Summary")

    if not st.session_state.meeting_summary:
        st.info("Summary will appear after meeting ends.")
        return

    st.markdown(st.session_state.meeting_summary)
