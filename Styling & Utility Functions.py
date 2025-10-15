%%writefile app.py
import streamlit as st
import json
import re

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="🧠 Visual Product Matcher", layout="centered", page_icon="🛍️")

# ---------- LOAD DATA ----------
with open("products.json", "r") as f:
    products = json.load(f)

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

# ---------- UTILITIES ----------
def extract_keywords(text):
    """Extract keywords from filename or URL."""
    name = re.split(r'[./_?=&-]+', text.split('/')[-1].lower())
    return [w for w in name if w and w.isalnum()]

def search_products(keywords):
    results = []
    for p in products:
        match_count = sum(any(k in t.lower() for t in p["tags"]) for k in keywords)
        if match_count > 0:
            p["score"] = match_count
            results.append(p)
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

# ---------- MAIN UI ----------
st.title("🛍️ Visual Product Matcher")
st.markdown("Upload an image or paste a URL to find visually similar products based on keywords in the file name or URL.")

col1, col2 = st.columns(2)
query = None
preview = None

with col1:
    st.subheader("📁 Upload an Image")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg","jpeg","png"])
    if uploaded_file:
        preview = uploaded_file.name
        st.image(uploaded_file, width=200, caption="Uploaded Preview")
        query = uploaded_file.name

with col2:
    st.subheader("🌐 Or Paste Image URL")
    url_input = st.text_input("Enter image URL")
    if url_input:
        st.image(url_input, width=200, caption="URL Preview")
        query = url_input

if query:
    if st.button("🔍 Search Similar Products"):
        st.info("Searching for similar items...")
        keywords = extract_keywords(query)
        results = search_products(keywords)

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
