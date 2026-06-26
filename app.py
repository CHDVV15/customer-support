import streamlit as st
from chatbot import CustomerSupportChatbot

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Load Chatbot
# -----------------------------
@st.cache_resource
def load_chatbot():
    return CustomerSupportChatbot()

bot = load_chatbot()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("🤖 Customer Support Bot")

    st.markdown("""
Welcome to the AI-powered Customer Support Chatbot.

### Features
- Account Support
- Order Tracking
- Shipping Information
- Payments
- Returns & Refunds
- Human Escalation
""")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# Main Title
# -----------------------------
st.title("🤖 AI Customer Support Chatbot")

st.write(
    "Hello! I'm your virtual customer support assistant. "
    "How can I help you today?"
)

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------
prompt = st.chat_input("Type your question here...")

if prompt:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Typing animation
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = bot.get_response(prompt)

        if response["status"] == "success":
            bot_message = response["answer"]

        elif response["status"] == "escalate":
            bot_message = (
                "⚠️ " + response["answer"] +
                "\n\nPlease contact our customer support team for further assistance."
            )

        else:
            bot_message = (
                "❌ Sorry, something went wrong. "
                "Please try again later."
            )

        st.markdown(bot_message)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_message
        }
    )