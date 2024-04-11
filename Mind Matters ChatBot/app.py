import os
import streamlit as st
import google.generativeai as genai

# Set the path to your service account key file
#NOTE:just change the file path to the location of the json file on your device
keyfile_path = r"D:\Chatbot\fleet-bus-374306-8d45ec253fd9.json"

# Set the environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = keyfile_path

# Configure Gemini API
genai.configure(api_key=os.getenv("api key"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Mind Matters Chatbot")
st.header("Mind Matters Chatbot - Your Mental Health Buddy")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input text box
input_text = st.text_input("Input:", key="input")

# Submit button
submit_button = st.button("Ask me a question!")

# If the user submits the input
if submit_button and input_text:
    # Get Gemini response
    response = get_gemini_response(input_text)
    
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input_text))
    
    # Display response
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display chat history
st.subheader("Chat History:")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
