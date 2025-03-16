import streamlit as st
import pandas as pd
import nltk
import pickle
import string
import plotly.express as px
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download NLTK resources
nltk.download('punkt')

# Initialize Porter Stemmer
ps = PorterStemmer()

# Function to preprocess text
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = [i for i in text if i.isalnum()]
    y = [ps.stem(i) for i in y if i not in stopwords.words('english') and i not in string.punctuation]

    return " ".join(y)

# Load trained tokenizer and model
tk = pickle.load(open("transform.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

# Initialize history storage
if "history" not in st.session_state:
    st.session_state.history = []

# Streamlit UI
st.set_page_config(page_title="SMS Spam Detection", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "History", "About Us", "Statistics"])

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f7f3e9;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #d9534f;
        text-align: center;
    }
    .subheading {
        font-size: 18px;
        font-weight: bold;
        color: #5a5a5a;
        text-align: center;
    }
    .stTextInput > div > div > input {
        font-size: 16px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #d9534f;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 8px 15px;
    }
    .result {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Home Page
if page == "Home":
    st.markdown('<p class="title">📩 SMS Spam Detection Model</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheading">Made by Pratiksha Waghmode</p>', unsafe_allow_html=True)

    # Input field
    input_sms = st.text_input("Enter the SMS below:", placeholder="Type your message here...")

    # Predict Button
    if st.button('Predict 🚀'):
        if input_sms.strip():  # Check if input is not empty
            transformed_sms = transform_text(input_sms)
            vector_input = tk.transform([transformed_sms])
            result = model.predict(vector_input)[0]

            # Store history
            prediction_text = "Spam 🚨" if result == 1 else "Not Spam ✅"
            st.session_state.history.append({"Message": input_sms, "Prediction": prediction_text})

            # Display results
            if result == 1:
                st.markdown('<p class="result" style="color: red;">🚨 Spam</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="result" style="color: green;">✅ Not Spam</p>', unsafe_allow_html=True)
        else:
            st.warning("Please enter an SMS to analyze.")

# History Page
elif page == "History":
    st.markdown('<p class="title">📜 Prediction History</p>', unsafe_allow_html=True)

    if st.session_state.history:
        df_history = pd.DataFrame(st.session_state.history)
        st.dataframe(df_history)  # Display history as a table
    else:
        st.info("No history available yet. Start predicting!")

# About Us Page
elif page == "About Us":
    st.markdown('<p class="title">💡 About This Project</p>', unsafe_allow_html=True)
    st.write("""
    **Project:** SMS Spam Detection Model  
    **Developer:** Pratiksha Waghmode  
    **Technology Used:** Python, Streamlit, NLP, Machine Learning  
    **Purpose:** This project helps in detecting spam messages using NLP techniques and Machine Learning models.  
    """)

# Statistics Page
elif page == "Statistics":
    st.markdown('<p class="title">📊 Spam vs. Ham Analysis</p>', unsafe_allow_html=True)

    # Sample Data (Replace with real stats)
    spam_count = 35
    ham_count = 65
    df_stats = pd.DataFrame({"Type": ["Spam", "Not Spam"], "Count": [spam_count, ham_count]})

    # Pie Chart
    fig = px.pie(df_stats, names="Type", values="Count", title="Spam vs. Not Spam Messages", color="Type",
                 color_discrete_map={"Spam": "red", "Not Spam": "green"})
    st.plotly_chart(fig)

    # Bar Chart
    fig_bar = px.bar(df_stats, x="Type", y="Count", title="Message Type Distribution", color="Type",
                     color_discrete_map={"Spam": "red", "Not Spam": "green"})
    st.plotly_chart(fig_bar)
