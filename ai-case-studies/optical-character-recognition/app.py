import streamlit as st
import base64
from ocr_helper import process_ocr
from upload_helper import image_upload
from clear_state import add_clear_button

# Helper function to load and encode image
@st.cache_data
def load_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Streamlit app configuration
st.set_page_config(
    page_title="Optical Character Recognition (OCR): Gemma-3", 
    page_icon=":guardsman:", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Title and description in main area
header_image_base64 = load_image_as_base64("./assets/gemma3.png")
st.markdown(f"""
    # <img src="data:image/png;base64,{header_image_base64}" width="50" style="vertical-align: -12px;"> Optical Character Recognition (OCR): Gemma-3
""", unsafe_allow_html=True)

# Add clear button to top right
add_clear_button()

st.markdown('<p style="margin-top: -20px;">Extract structured text from images using Multimodal Gemma-3 Vision!</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar for image upload
with st.sidebar:
    uploaded_file, image = image_upload()

    if uploaded_file is not None:
        if st.button("Extract Text 🔍", type="primary"):
            with st.spinner("Processing image..."):
                try:
                    ocr_result = process_ocr(uploaded_file.getvalue())
                    st.session_state['ocr_result'] = ocr_result
                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")

# Main content area for results
if 'ocr_result' in st.session_state:
    st.markdown(st.session_state['ocr_result'])
else:
    st.info("Upload an image and click 'Extract Text 🔍' to display the extracted text here.")