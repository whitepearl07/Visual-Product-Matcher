# app.py
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Visual Product Matching", page_icon="🛍️", layout="centered")

st.title("Visual Product Matching")
st.write("Upload an image or provide an image URL to find visually similar products.")

# Choice: Upload or URL
input_type = st.radio("Choose input method:", ("Image URL"))

image = None

if input_type == "Image URL":
    image_url = st.text_input("Enter image URL:")
    if image_url:
        try:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
        except Exception as e:
            st.error("Unable to load image from URL. Please check the URL.")

# Display image and placeholder matching results
if image:
    st.image(image, caption="Input Image", use_column_width=True)
    
    # TODO: Add your visual product matching logic here
    st.write("Searching for similar products...")

    # Example placeholder results
    st.image(image, caption="Similar Product 1", width=200)
    st.image(image, caption="Similar Product 2", width=200)
    st.image(image, caption="Similar Product 3", width=200)

st.write("Made with ❤️ using Streamlit")
