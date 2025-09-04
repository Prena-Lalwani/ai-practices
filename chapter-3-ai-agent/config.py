import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("No API key found. Please set GEMINI_API_KEY or GOOGLE_API_KEY in .env")

# Configure Gemini
genai.configure(api_key=api_key)
