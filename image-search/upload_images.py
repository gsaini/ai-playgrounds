import streamlit as st
from images_store import ImagesStore

st.title("Upload Images")
uploaded_images = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_images:
    for uploaded_image in uploaded_images:
        doc_id = ImagesStore.upload_images(uploaded_image)
        st.image(ImagesStore.get_image_path_by_id(doc_id), caption=ImagesStore.get_by_id(doc_id).page_content)

    # for doc_id in doc_ids:
    st.success("Images uploaded successfully!")