import speech_recognition as sr
from faster_whisper import WhisperModel
import os
import re

# chodon 64 NVIDIA gpu na thakle Cpu e selected valo, edi muloto whister stt er jnno lagbo.
MODEL_SIZE = "base.en" 
DEVICE = "cpu" 
COMPUTE_TYPE = "int8" 

print(f"[EARS] Loading Whisper Model ({MODEL_SIZE})...")
model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)
print("[EARS] Model Loaded.")

r = sr.Recognizer()
r.dynamic_energy_threshold = True
r.energy_threshold = 300
r.pause_threshold = 1.0

def get_best_mic():
    mics = sr.Microphone.list_microphone_names()
    for i, name in enumerate(mics):
        if "QCY" in name or "Headset" in name:
            return i, name
    return None, "Default System Mic"

def listen():
    mic_index, mic_name = get_best_mic()
    
    try:
        with sr.Microphone(device_index=mic_index) as source:
            print(f"\n[EARS] Listening on: {mic_name}")
            r.adjust_for_ambient_noise(source, duration=0.5)
            
           
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("[EARS] Transcribing...")

            
            with open("command.wav", "wb") as f:
                f.write(audio.get_wav_data())

            
            segments, info = model.transcribe("command.wav", beam_size=5)
            full_text = "".join([segment.text for segment in segments]).strip()
            
            
            if not full_text: 
                return None
            
            
            if not re.search(r'[a-zA-Z]', full_text):
                
                return None

          
            if full_text.lower() in ["you.", "thank you.", "bye.", "."]:
                return None


            print(f"You said: {full_text}")
            
         
            if os.path.exists("command.wav"):
                os.remove("command.wav")

            return full_text.lower()
            
    except sr.WaitTimeoutError:
        return None
    except Exception as e:
        print(f"[EARS] Error: {e}")
        return None