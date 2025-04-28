import streamlit as st

from images_store import ImagesStore

st.title("Image Search")
query = st.text_input("Enter a query to search for images:")

if query:
    results = ImagesStore.retrieve_docs_by_query(query) # Retrieve documents based on the query
    if results:
        for doc in results:
            image_path = ImagesStore.get_image_path_by_id(doc.id)
            st.image(image_path, caption=doc.page_content)  # Display the image with its description
    else:
        st.write("No images found for the given query.")