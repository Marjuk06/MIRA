import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# PERSONALITY: Smart, capable, and slightly sassy.
sys_instruction = """
You are MIRA.
- You are an advanced AI agent capable of controlling the user's PC.
- Be concise. Don't ramble.
- If the user asks for a feature you have, confirm it briefly (e.g., "On it.", "Drafting that now.").
"""

def think(user_text):
    try:
        # We switch to 'gemini-1.5-flash' which is the standard STABLE model
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=sys_instruction + f"\nUser: {user_text}\nMIRA:",
        )
        return response.text.replace("*", "")
    except Exception as e:
        print(f"[Brain Error] {e}")
        return "My connection is fuzzy. One moment."