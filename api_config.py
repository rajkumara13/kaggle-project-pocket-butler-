import google.generativeai as genai
import os

# Load API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "Your api key")

genai.configure(api_key=GEMINI_API_KEY)

MODEL = "gemini-1.5-flash"
