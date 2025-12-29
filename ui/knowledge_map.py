import streamlit as st


def render_knowledge_map():
    st.subheader("🧠 Live Knowledge Map")

    if not st.session_state.knowledge_items:
        st.info("No key concepts detected yet.")
        return

    for item in st.session_state.knowledge_items:
        with st.expander(item["term"]):
            st.write(item["explanation"])
