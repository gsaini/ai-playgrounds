import streamlit as st

def add_clear_button():
    """
    Adds a clear button to the Streamlit app, which clears the session state and reruns the app.
    """
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("Clear 🗑️"):
            st.session_state.pop('ocr_result', None)
            st.rerun()