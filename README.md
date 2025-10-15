
## 🌐 Live Demo

Check out the live version of **Visual Product Matching** here:  

[🔗 Open Live App](https://visual-appuct-matcher-msgomszvqtdppghkdjabdl.streamlit.app/)


# 🛍️ ProductMatch – Smart Product Recommendation & Matching App

## 📖 Overview

**ProductMatch** is an interactive web app built with **Streamlit** that helps users explore and compare products efficiently. It intelligently matches similar products based on tags, prices, and attributes — offering an intuitive way to find related or alternative items.

## 🚀 Features

* **Product Similarity Matching:** Automatically find and display similar products using data-driven matching logic.
* **Dynamic Filtering:** Search and filter products based on tags, categories, or pricing.
* **Interactive Interface:** Built with Streamlit for a fast, beautiful, and easy-to-use frontend.
* **Cloud Access:** Hosted via **ngrok** for quick online sharing and demo access.
* **Data Handling:** Reads and processes structured product data (JSON/CSV) to create relationships between items.

## 🧠 Technologies Used

* **Python 3.10+**
* **Streamlit** – for the interactive web interface
* **Pandas / NumPy** – for data analysis and manipulation
* **Ngrok** – to share the local Streamlit app online
* **JSON / CSV** – for product dataset management

## 📂 Project Structure

```
ProductMatch.ipynb       # Jupyter Notebook with Streamlit setup and logic
products.json            # Sample product dataset (bags, bedsheets, etc.)
requirements.txt         # List of dependencies (optional)
```

## ⚙️ How to Run

```bash
# 1. Install dependencies
pip install streamlit pandas numpy pyngrok

# 2. Run the app
streamlit run ProductMatch.ipynb

# 3. (Optional) Expose app online using ngrok
ngrok authtoken YOUR_TOKEN
ngrok http 8501
```

## 🌐 Example Use Cases

* E-commerce product recommendation
* Price comparison systems
* Tag-based similarity detection
* Smart catalog browsing for online stores

## 🧩 Future Enhancements

* Integrate **image similarity** using deep learning
* Add **user personalization** (favorites, history)
* Support for **multiple datasets** (fashion, electronics, etc.)

