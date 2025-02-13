import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyDBTW5yuxE8k5S7UaZGoLrLZtfyPmMGIsw")

# System prompt for the AI model
sys_prompt = """You are a helpful AI Tutor for Data Science. 
                Students will ask you doubts related to various topics in data science.
                You are expected to reply in as much detail as possible. 
                Make sure to take examples while explaining a concept.
                In case if a student ask any question outside the data science scope, 
                politely decline and tell them to ask the question from data science domain only.
                Always include a helpful statement at the end saying that 
                'In case if your query is not resolved, feel free to click on this link:
                innomatics.in to get in touch with our mentor in a 1:1 zoom call'"""

# List available models and print them (for debugging)
available_models = genai.list_models()
print("Available models:", available_models)  # Print available models for debugging

# Replace with a valid model after checking the available models list
gemini_model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=sys_prompt)

# Set up Streamlit app
st.title("Data Science/AI TUTOR")

# Input field for user query
user_input = st.text_area("Enter your query/issue", placeholder="Explain the concept of for loops")

# Button to trigger the response
btn_click = st.button("Click Me!")

# When button is clicked, generate and display the response
if btn_click:
    # Use the correct method to generate content
    response = gemini_model.generate_content(user_input)  # Ensure method is correct
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)
