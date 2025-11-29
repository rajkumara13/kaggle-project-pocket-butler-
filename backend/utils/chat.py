import os
import google.generativeai as genai

# Load API Key (correct env variable name)
genai.configure(api_key="AIzaSyBUrpZ5V-bsn25ZSqYAyPk9zceZ3XjyetY")

# Use a valid Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

def ai_chat(user_text):
    try:
        response = model.generate_content(user_text)
        return response.text
    except Exception as e:
        return f"AI Error: {e}"
