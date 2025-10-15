import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Visual Product Matching", page_icon="🛍️", layout="centered")

st.title("Visual Product Matching")
st.write("Upload an image, and this app will find visually similar products.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # TODO: Add your visual product matching logic here
    st.write("Searching for similar products...")

    # Example placeholder results
    st.image(image, caption="Similar Product 1", width=200)
    st.image(image, caption="Similar Product 2", width=200)
    st.image(image, caption="Similar Product 3", width=200)

st.write("Made with ❤️ using Streamlit")
