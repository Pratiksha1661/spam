import nltk
import streamlit as st
import pickle 
import string
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

# Streamlit UI
st.set_page_config(page_title="SMS Spam Detection", layout="wide")

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

# Title
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

        # Display results
        if result == 1:
            st.markdown('<p class="result" style="color: red;">🚨 Spam</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="result" style="color: green;">✅ Not Spam</p>', unsafe_allow_html=True)
    else:
        st.warning("Please enter an SMS to analyze.")

