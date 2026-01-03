import speech_recognition as sr

# 1. Setup the Microphone ONCE (prevents lag)
r = sr.Recognizer()
r.energy_threshold = 4000 # Fixes sensitivity
r.dynamic_energy_threshold = True

def listen():
    try:
        # Use your QCY Headset (ID 2). 
        # If this fails, change index=2 to index=None (default mic)
        with sr.Microphone(device_index=2) as source:
            print("Listening...")
            
            # Listen (Wait up to 5s for silence, listen for 8s max)
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            
            print("Recognizing...")
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
            
    except sr.WaitTimeoutError:
        return None
    except sr.UnknownValueError:
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None