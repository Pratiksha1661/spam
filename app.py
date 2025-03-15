import streamlit as st
import plotly.express as px
import base64

# Function to set background image
def set_bg(image_file):
    with open(image_file, "rb") as img:
        encoded_string = base64.b64encode(img.read()).decode()
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

# Set page title and layout
st.set_page_config(page_title="SMS Spam Detection", layout="wide")

# Apply background image
set_bg("image.png")

# Sidebar Navigation
st.sidebar.markdown("### 📌 Navigation", unsafe_allow_html=True)
page = st.sidebar.radio("Go to:", ["Home", "History", "About Us", "Statistics"])

# Home Page
if page == "Home":
    st.markdown("<h2 style='text-align: center; color: red;'>📩 SMS Spam Detection Model</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Made by Pratiksha Waghmode</h4>", unsafe_allow_html=True)

    st.write("### Enter the SMS below:")
    message = st.text_area("Type your message here...")

    if st.button("🚀 Predict", help="Click to classify as Spam or Ham"):
        # Placeholder for model prediction (replace with actual model logic)
        st.success("✅ Prediction: This is NOT spam!")

# History Page
elif page == "History":
    st.markdown("## 🔍 Prediction History")
    st.write("Previous predictions will be displayed here.")

# About Us Page
elif page == "About Us":
    st.markdown("## ℹ️ About Us")
    st.write("This app was developed to detect SMS spam messages using Machine Learning.")

# Statistics Page
elif page == "Statistics":
    st.markdown("## 📊 Model Statistics")

    # Sample data
    data = {"Category": ["Spam", "Not Spam"], "Count": [1200, 3800]}
    df = px.data.tips()
    fig = px.pie(values=data["Count"], names=data["Category"], title="Spam vs Not Spam Distribution", color=data["Category"])
    st.plotly_chart(fig)
