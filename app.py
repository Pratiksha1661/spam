import streamlit as st

# Set page title and layout
st.set_page_config(page_title="SMS Spam Detection", layout="wide")

# Sidebar Navigation
st.sidebar.markdown("### 📌 Navigation", unsafe_allow_html=True)
page = st.sidebar.radio("Go to:", ["Home", "History", "About Us"])

# Home Page
if page == "Home":
    st.markdown("<h2 style='text-align: center; font-size:36px; color: red;'>📩 SMS Spam Detection Model</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; font-size:20px; color: gray;'>Made by Pratiksha Waghmode</h4>", unsafe_allow_html=True)

    st.write("### Enter the SMS below:")
    message = st.text_area("Type your message here...", height=100)

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
