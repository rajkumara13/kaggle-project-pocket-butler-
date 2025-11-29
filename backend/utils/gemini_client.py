import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

MODEL = "gemini-1.5-flash"

def ask_gemini(prompt):
    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)
    return response.text
