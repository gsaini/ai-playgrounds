import streamlit as st
from PIL import Image

def image_upload():
    """
    Creates a sidebar widget for uploading an image in a Streamlit app.

    Returns:
        tuple: A tuple containing the uploaded file and the PIL Image object, or (None, None) if no file is uploaded.
    """
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")
        return uploaded_file, image

    return None, None