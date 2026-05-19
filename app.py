import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="AI Chatbot with Memory",
    page_icon="💬",
    layout="centered"
)

st.title("Conversational AI Chatbot")
st.caption("A sateful chatbot that remebers your conversation")
