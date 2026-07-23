from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI Assistant.")
    ]

# Show previous messages
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Input
user_input = st.chat_input("Type your message...")

if user_input:

    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )

    response = model.invoke(st.session_state.chat_history)

    st.session_state.chat_history.append(
        AIMessage(content=response.content)
    )

    st.rerun()

