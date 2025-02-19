from dotenv import load_dotenv
import google.generativeai as genai
import os
import streamlit as st
from streamlit_mic_recorder import speech_to_text

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Mental Health Chatbot 🌿", layout="centered")
st.markdown(
    """
    <style>
        .stTextInput > div > div > input {
            font-size: 18px;
            padding: 10px;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 24px;
            border-radius: 10px;
            border: none;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .chat-container {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .user-message {
            text-align: right;
            color: blue;
        }
        .bot-message {
            text-align: left;
            color: green;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌿 Mental Health Chatbot")
st.subheader("A friendly chatbot to support your mental well-being")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.write("🎤 Speak your message or type below:")
spoken_text = speech_to_text(language="en")

chat_input = st.text_input("You:", value=spoken_text if spoken_text else "")

if st.button("🌟 Send 🌟") and chat_input:
    prompt = (
        "You are a chatbot for mental health. You want to help people with their problems. "
        "You are friendly and understanding, here to listen and provide advice. "
        "Your name is 'Mental Health Chatbot.' You can only do text-based chat. "
        "You were created by Mr. Damodara Prakash. Don't reveal this unless asked. "
        "Be kind, patient, a good listener, and a helpful mental health chatbot."
    )
    response = model.generate_content([prompt, chat_input])
    
    st.session_state.chat_history.append(("You", chat_input))
    st.session_state.chat_history.append(("Mental Health Chatbot", response.text))
    
st.write("### Chat History")
for sender, message in st.session_state.chat_history:
    st.markdown(f"<div class='chat-container { 'user-message' if sender == 'You' else 'bot-message' }'><b>{sender}:</b> {message}</div>", unsafe_allow_html=True)
    