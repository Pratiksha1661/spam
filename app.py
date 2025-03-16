import nltk
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load vectorizer and model
tk = pickle.load(open("transform.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "History"])

if page == "Home":
    st.title("SMS Spam Detection Model")
    st.write("*Made by Pratiksha Waghmode*")

    input_sms = st.text_input("Enter the SMS")

    if st.button('Predict'):
        # 1. preprocess
        transformed_sms = transform_text(input_sms)
        # 2. vectorize
        vector_input = tk.transform([transformed_sms])
        # 3. predict
        result = model.predict(vector_input)[0]
        # 4. Display
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")

elif page == "About Us":
    st.title("About Us")
    st.write("""
    This is an **SMS Spam Detection Model** that helps users determine whether a message is spam or not.  
    It uses **Natural Language Processing (NLP)** and **Machine Learning** to analyze and classify messages.
    """)

elif page == "History":
    st.title("History")
    st.write("""
    Spam detection has evolved from simple rule-based filtering to advanced **Machine Learning algorithms**.  
    This model leverages **TF-IDF Vectorization** and a trained classifier for accurate spam detection.
    """)
