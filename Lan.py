import streamlit as st
from googletrans import Translator

st.title("🌍 Simple Translate Chatbot")

# Translator
translator = Translator()

# User input
user_text = st.text_input("Type your message:")

# Target language
lang = st.selectbox("Translate to:", ["ta", "hi", "fr", "de", "es", "en"])
st.caption("Languages: ta=Tamil, hi=Hindi, fr=French, de=German, es=Spanish, en=English")

if st.button("Translate"):
    if user_text:
        # Translate
        translated = translator.translate(user_text, dest=lang)
        st.write("**You:**", user_text)
        st.write("**Bot:**", translated.text)
