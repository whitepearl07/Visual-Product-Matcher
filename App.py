%%writefile app.py
import streamlit as st
from PIL import Image
import numpy as np
import json
import torch
from torchvision import models, transforms
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="🧠 Visual Product Matcher", layout="centered", page_icon="🛍️")

# ---------- LOAD DATA ----------
with open("products.json", "r") as f:
    products = json.load(f)

# Precompute feature vectors for products
# products.json should have 'image' field (URL/local path) and 'name' etc.

# ---------- IMAGE MODEL ----------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(pretrained=True)
model.fc = torch.nn.Identity()  # remove final classification layer
model = model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def extract_features(image):
    img = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        feat = model(img).cpu().numpy()[0]
    return feat / np.linalg.norm(feat)

# Precompute product features once
if "features" not in st.session_state:
    st.session_state["features"] = []
    for p in products:
        try:
            img = Image.open(p['image']).convert('RGB')
            feat = extract_features(img)
            st.session_state["features"].append(feat)
        except:
            st.session_state["features"].append(np.zeros(512))  # fallback

# ---------- STYLING ----------
st.markdown("""
<style>
body {background:#f5f7fa;font-family:'Inter',sans-serif;}
h1{text-align:center;color:#333;}
.upload-box{
  display:flex;justify-content:center;gap:40px;
  background:#fff;padding:25px;border-radius:12px;
  box-shadow:0 2px 8px rgba(0,0,0,0.05);
}
.results{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(180px,1fr));
  gap:20px;margin-top:20px;
}
.product-card{
  background:#fff;border-radius:10px;
  padding:12px;text-align:center;
  box-shadow:0 2px 6px rgba(0,0,0,0.08);
}
.product-card img{
  width:100%;border-radius:8px;
  height:160px;object-fit:cover;
}
.stTextInput>div>div>input{
  border-radius:8px;padding:6px 10px;
  border:1px solid #ccc;
}
.stButton>button{
  background:#007bff;color:white;border:none;
  border-radius:6px;padding:6px 14px;cursor:pointer;
}
.stButton>button:hover{background:#0056b3;}
</style>
""", unsafe_allow_html=True)

# ---------- MAIN UI ----------
st.title("🛍️ Visual Product Matcher")
st.markdown("Upload an image or paste a URL to find visually similar products based on actual visual features.")

col1, col2 = st.columns(2)
query_image = None

with col1:
    st.subheader("📁 Upload an Image")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg","jpeg","png"])
    if uploaded_file:
        query_image = Image.open(uploaded_file).convert('RGB')
        st.image(query_image, width=200, caption="Uploaded Preview")

with col2:
    st.subheader("🌐 Or Paste Image URL")
    url_input = st.text_input("Enter image URL")
    if url_input:
        try:
            query_image = Image.open(requests.get(url_input, stream=True).raw).convert('RGB')
            st.image(query_image, width=200, caption="URL Preview")
        except:
            st.warning("Unable to load image from URL")

def find_similar(query_img, top_n=5):
    q_feat = extract_features(query_img)
    dists = [np.linalg.norm(q_feat - f) for f in st.session_state["features"]]
    idxs = np.argsort(dists)[:top_n]
    return [products[i] for i in idxs]

if query_image:
    if st.button("🔍 Search Similar Products"):
        st.info("Searching for similar items...")
        results = find_similar(query_image, top_n=5)

        if results:
            st.subheader("🛒 Matching Products")
            st.markdown('<div class="results">', unsafe_allow_html=True)
            for p in results:
                st.markdown(f"""
                <div class="product-card">
                  <img src="{p['image']}" alt="{p['name']}"/>
                  <p><b>{p['name']}</b></p>
                  <p>{", ".join(p['tags'])}</p>
                  <p style="color:green;"><b>{p['price']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("No matching products found.")
else:
    st.info("Upload an image or paste a URL to start searching.")
