import streamlit as st 
import datetime

# Title
st.title("💬simple Chatbot ")
st.write("Simple commands like: **hello, your name, time,date, exit**")

# Keep chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Simple bot logic
    if "hello" in prompt.lower():
        response = "Hello! How are you?"
    elif "your name" in prompt.lower():
        response = "I am your simple chatbot 🤖"
    elif "time" in prompt.lower():
        response=time = datetime.datetime.now().strftime("%I:%M %p")
    elif "date" in prompt.lower():
        response = datetime.datetime.now().strftime("%B %d, %Y")
    elif "bye" in prompt.lower() or "exit" in prompt.lower():
        response = "Goodbye! Have a great day!"
    else:
        response = "I don’t understand that yet."

    # Add bot response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)

