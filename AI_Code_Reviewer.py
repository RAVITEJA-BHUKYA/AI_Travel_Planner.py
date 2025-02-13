import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyDBTW5yuxE8k5S7UaZGoLrLZtfyPmMGIsw")  # Replace with your own API key

# System prompt for the AI model to review code
sys_prompt = """You are an AI code reviewer. 
                Review this Python code and identify any bugs or issues. Suggest fixes if necessary.
                Provide detailed explanations for the identified bugs and the proposed fixes. 
                Format the response as 'Bug Report' followed by the 'Fixed Code'. 
                Only focus on Python code issues and provide suggestions on how to fix them.
                """

# Streamlit UI for user input
st.title("AI Code Reviewer")

# Input field for user code
code_input = st.text_area("Enter your Python code here...", height=100)

# Button to trigger the review
if st.button("Generate Review"):
    if code_input:
        # Generate the prompt directly here
        prompt = f"Review the following Python code and identify any issues. Suggest fixes if necessary:\n\n{code_input}"
        
        # Send the prompt to the AI model for review
        response = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=sys_prompt).generate_content(prompt)
        
        # Display the review
        st.subheader("Code Review")
        st.write(response.text)
    else:
        st.error("Please enter some code to review.")
