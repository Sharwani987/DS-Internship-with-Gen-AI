import joblib
import streamlit as st
import re

# Load trained model and vectorizer
model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

st.title("Flipkart Review Sentiment Analyzer")

# Simple preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # remove punctuation/numbers
    return text.strip()

# Text box for user input
user_input = st.text_area("Enter a review:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a review before predicting.")
    else:
        # Clean the input
        cleaned = preprocess_text(user_input)
        
        # If cleaning results in empty string, block prediction
        if cleaned == "":
            st.warning("⚠️ Your review only had symbols/numbers. Please enter valid text.")
        else:
            # Transform input using TF-IDF
            vectorized = tfidf.transform([cleaned])
            
            # Predict sentiment
            prediction = model.predict(vectorized)[0]
            
            st.success(f"Predicted Sentiment: {prediction}")