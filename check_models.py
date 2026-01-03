import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("Checking available models...")
try:
    
    for m in client.models.list():
       
        if "generateContent" in m.supported_actions:
            print(f"- {m.name}")
            
except Exception as e:
    print(f"Error: {e}")