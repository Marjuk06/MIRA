import ears
import brain
import mouth
import skills
import time


context = {
    "last_app": "browser",
    "whatsapp_mode": False
}

def run_mira():
    mouth.say("MIRA Agent Systems Online.")
    
    while True:
        if mouth.is_speaking():
            time.sleep(0.1)
            continue

        user_input = ears.listen()
        
        if user_input:
            text = user_input.lower()
            # Code Base er dictinary edi, majhe majhe dekhba vulval word dhore tts, eita oida fix krbe
            corrections = {
                "opirogic": "opera gx",
                "up your gx": "opera gx",
                "gx": "opera gx",
                "opera": "opera gx",
                "hot set": "whatsapp",
                "mess is": "message",  # Fixes "Mess is high"
                "mess": "message",
                "code": "visual studio code"
            }
            
            for mistake, real_word in corrections.items():
                if mistake in text:
                    text = text.replace(mistake, real_word)
            
            print(f"DEBUG: Intent -> {text}")

            # Message send er age confirmation lagbe
            if context["whatsapp_mode"]:
                if "send" in text or "yes" in text or "confirm" in text:
                    mouth.say(skills.send_message())
                    context["whatsapp_mode"] = False 
                elif "cancel" in text or "no" in text:
                    mouth.say("Cancelled.")
                    context["whatsapp_mode"] = False
                else:
                    mouth.say("Say 'Send it' or 'Cancel'.")
                continue 

            
            if "exit" in text or "sleep" in text:
                mouth.say("Goodnight.")
                break

            # Shyata vanga whatsapp system integrate krsi, mainly eida pid re target na kore universal commands debe, spotify my chalai na, so jani na
            is_messaging = (
                text.startswith("message") or 
                text.startswith("text") or
                ("whatsapp" in text and ("say" in text or "send" in text or "tell" in text))
            )

            if is_messaging:
                mouth.say("On it...")
                data = brain.extract_details(text) 
                contact = data.get("contact", "Unknown")
                msg = data.get("message", "")
                
                if contact == "Unknown":
                    mouth.say("Who should I message?")
                else:
                    mouth.say(skills.draft_whatsapp_msg(contact, msg))
                    context["whatsapp_mode"] = True

            
            elif "search" in text:
                query = text.replace("search", "").strip()
                mouth.say(skills.search_in_active_window(query, context["last_app"]))

            
            elif "open" in text:
                raw_name = text.replace("open", "").strip()
                name = raw_name

                if " in " in name:
                    site_name = name.split(" in ")[0].strip()
                    mouth.say(skills.open_website(site_name))
                
                elif name in ["youtube", "facebook", "twitter", "instagram", "reddit"]:
                    mouth.say(skills.open_website(name))
                    context["last_app"] = "browser"
                
                elif "spotify" in name:
                    mouth.say(skills.open_app("spotify"))
                    context["last_app"] = "spotify"
                
                else:
                    mouth.say(skills.open_app(name))
                    context["last_app"] = "general"

            
            elif "play" in text or "pause" in text:
                skills.play_media()
            elif "skip" in text:
                skills.skip_song()
            elif "close window" in text:
                skills.close_window()

          
            else:
                reply = brain.think(text)
                mouth.say(reply)
            
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        run_mira()
    except KeyboardInterrupt:
        print("\nForce Quit.")
    except Exception as e:
        print(f"Critical Error: {e}")