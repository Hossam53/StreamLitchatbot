import openai
import streamlit as st

# Set the page title
st.header("AI Conversation Simulator")

# Configure the API key from Streamlit's secrets
openai.api_key = st.secrets["SECRET_API_KEY"]

# Initializing the AI model in session state if not already present
if "ai_model_version" not in st.session_state:
    st.session_state["ai_model_version"] = "text-davinci-003"

# Chat input for the user
user_input = st.text_input("Your message:", key="user_input")

# If user provides input, process it
if user_input:
    # Show user's message in the chat
    with st.expander("You say:"):
        st.write(user_input)

    # AI assistant's turn to reply
    with st.expander("AI replies:"):
        # Placeholder for the AI's response
        response_placeholder = st.empty()
        # Generate the response from OpenAI's API
        ai_response = openai.ChatCompletion.create(
            model=st.session_state["ai_model_version"],
            messages=[{"role": "user", "content": user_input}]
        )
        # Extracting the text response from the API response
        ai_text_response = ai_response.choices[0].message['content']
        # Display the AI's response
        response_placeholder.write(ai_text_response)
