import ears
import brain
import mouth
import skills
import time

# STATE VARIABLES (Memory)
# These remember what MIRA is currently doing
context = {
    "last_app": None,        # What did we just open?
    "whatsapp_mode": False   # Are we waiting to send a message?
}

def run_mira():
    mouth.say("MIRA Agent Systems Online.")
    
    while True:
        user_input = ears.listen()
        
        if user_input:
            print(f"User: {user_input}")
            text = user_input.lower()

            # --- 1. WHATSAPP CONFIRMATION MODE ---
            if context["whatsapp_mode"]:
                if "send" in text or "yes" in text or "confirm" in text:
                    mouth.say(skills.send_message())
                    context["whatsapp_mode"] = False # Reset mode
                elif "cancel" in text or "no" in text:
                    mouth.say("Cancelled.")
                    context["whatsapp_mode"] = False
                else:
                    mouth.say("Still waiting. Say 'Send it' or 'Cancel'.")
                continue # Skip the rest of the loop

            # --- 2. EXIT ---
            if "exit" in text or "sleep" in text:
                mouth.say("Goodnight.")
                break

            # --- 3. WHATSAPP AUTOMATION ---
            # Command: "Open WhatsApp and say Hi to Fahad"
            elif "whatsapp" in text and "say" in text:
                try:
                    # Extract name and message roughly
                    # This splits the sentence at "say"
                    parts = text.split("say") 
                    message_part = parts[1].strip() # "Hi to Fahad"
                    
                    # Simple heuristic: assume the last word is the name, rest is message
                    # Or better: You say "Message Fahad saying Hi"
                    # Let's try to be smart:
                    if "to" in message_part:
                        msg, contact = message_part.split(" to ")
                    else:
                        contact = "Unknown"
                        msg = message_part

                    mouth.say(skills.draft_whatsapp_msg(contact, msg))
                    context["whatsapp_mode"] = True # ENABLE CONFIRMATION MODE
                except:
                    mouth.say("I couldn't understand who to message. Try saying 'Open WhatsApp' first.")

            # --- 4. CONTEXT SEARCH (The "Search IN THERE" feature) ---
            # If user says "Search X" and we know we are in YouTube/Spotify
            elif "search" in text and ("youtube" not in text and "google" not in text):
                query = text.replace("search", "").strip()
                mouth.say(skills.search_in_active_window(query))

            # --- 5. OPEN APPS / SITES ---
            elif "open" in text:
                name = text.replace("open", "").strip()
                if "youtube" in name:
                    mouth.say(skills.open_website("youtube"))
                    context["last_app"] = "youtube"
                elif "spotify" in name:
                    mouth.say(skills.open_app("spotify"))
                    context["last_app"] = "spotify"
                elif "whatsapp" in name:
                    mouth.say(skills.open_app("whatsapp"))
                else:
                    mouth.say(skills.open_app(name))

            # --- 6. MEDIA CONTROLS ---
            elif "play" in text or "pause" in text:
                mouth.say(skills.play_media())
            elif "skip" in text or "next song" in text:
                mouth.say(skills.skip_song())

            # --- 7. UTILITIES ---
            elif "close window" in text:
                mouth.say(skills.close_window())
            elif "switch tab" in text:
                mouth.say(skills.switch_tab())

            # --- 8. BRAIN (Fall back to AI) ---
            else:
                reply = brain.think(text)
                print(f"MIRA: {reply}") 
                mouth.say(reply)
            
        time.sleep(0.2)

if __name__ == "__main__":
    run_mira()