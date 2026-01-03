import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("Checking available models...")
try:
    # Get the list of models valid for your key
    for m in client.models.list():
        # Only show models we can use for chat (generateContent)
        if "generateContent" in m.supported_actions:
            print(f"- {m.name}")
            
except Exception as e:
    print(f"Error: {e}")