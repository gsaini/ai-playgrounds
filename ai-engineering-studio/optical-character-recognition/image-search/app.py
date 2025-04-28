import streamlit as st

page = st.navigation([
    st.Page(title="Upload Images", icon="📤", page="upload_images.py"),
    st.Page(title="Image Search", icon="🔍", page="image_search.py"),
    # st.Page(title="Reverse Image Search", icon="🔄", page="/reverse-image-search")
])

page.run()

