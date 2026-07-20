import streamlit as st
st.set_page_config(page_title="Agentic Chatbot", page_icon="🤖")

st.title("🤖 Agentic Chatbot")
st.write("Welcome! Ask me anything.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
prompt = st.chat_input("Type your message...")

if prompt:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Simple Bot Logic
    if "hello" in prompt.lower():
        response = "Hello! 👋 How can I help you today?"
    elif "python" in prompt.lower():
        response = "Python is a powerful programming language used for AI, Web Development, Automation, and Data Science."
    elif "streamlit" in prompt.lower():
        response = "Streamlit is a Python framework used to build interactive web applications quickly."
    elif "bye" in prompt.lower():
        response = "Goodbye! Have a great day! 😊"
    else:
        response = "I'm still learning. Can you ask something else?"

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
