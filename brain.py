import os
import json
import time
from dotenv import load_dotenv

# Load .env for Gemini
load_dotenv()
history = []

sys_instruction = """
You are MIRA, an advanced AI agent controlling a PC.
- Be concise. 
- If the user asks to perform an action (open apps, play music), confirm briefly (e.g., "On it.", "Opening Spotify.").
"""

# Gemini INTEGRATION

from google import genai
import google.api_core.exceptions

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-2.0-flash"

def think(user_text):
    global history
    history.append(f"User: {user_text}")
    
    # Keep history short (last 6)
    context_block = "\n".join(history[-6:])
    
    try:
        response = client.models.generate_content(
            model=MODEL_NAME, 
            contents=sys_instruction + f"\n[CHAT HISTORY]\n{context_block}\nMIRA:",
        )
        reply = response.text.replace("*", "").strip()
        history.append(f"MIRA: {reply}")
        return reply

    except Exception as e:
        if "429" in str(e):
            print("[Brain] Rate limit hit. Waiting 5s...")
            time.sleep(5)
            return "I need a moment to recharge."
        print(f"[Brain Error] {e}")
        return "I'm having trouble connecting to Google."

def extract_details(text):
    try:
        prompt = f"""
        Extract 'contact' and 'message' from: "{text}"
        Return JSON only. Keys: contact, message.
        If unknown, use "Unknown".
        """
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        clean_json = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
    except:
        return {"contact": "Unknown", "message": text}


# LM STUDIO INTEGRATION
'''
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def think(user_text):
    global history
    

    history.append({"role": "user", "content": user_text})
    
    messages = [{"role": "system", "content": sys_instruction}] + history[-6:]

    try:
        response = client.chat.completions.create(
            model="local-model", 
            messages=messages,
            temperature=0.7,
        )
        
        reply = response.choices[0].message.content.strip()
        history.append({"role": "assistant", "content": reply})
        return reply

    except Exception as e:
        print(f"[Brain Error] {e}")
        return "I can't reach LM Studio. Is the server running?"

def extract_details(text):
    prompt = f"""
    Extract the 'contact' and 'message' from this command: "{text}"
    Return ONLY a JSON object. No other text.
    Format: {{"contact": "Name", "message": "The message content"}}
    If the contact is missing, use "Unknown".
    """
    
    try:
        response = client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system", "content": "You are a JSON extractor. Output valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
        )
        
        raw_text = response.choices[0].message.content.strip()
        clean_json = raw_text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)

    except Exception as e:
        print(f"[Extraction Error] {e}")
        return {"contact": "Unknown", "message": text}

'''