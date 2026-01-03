import asyncio
import edge_tts
import pygame
import threading
import time
import os

VOICE = "en-US-AriaNeural"


pygame.mixer.init()

async def generate_audio(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("response.mp3")

def play_audio_thread():
    """Plays audio in a separate thread so code doesn't freeze."""
    try:
        pygame.mixer.music.load("response.mp3")
        pygame.mixer.music.play()
        
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
      
        pygame.mixer.music.unload() 
    except Exception as e:
        print(f"Audio Error: {e}")

def say(text):
    print(f"MIRA: {text}")

    
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    
    
    try:
        pygame.mixer.music.unload()
    except:
        pass

   
    try:
        asyncio.run(generate_audio(text))
    except PermissionError:
        
        time.sleep(0.5)
        try:
            asyncio.run(generate_audio(text))
        except:
            print("Audio file locked. Skipping voice.")
            return

   
    t = threading.Thread(target=play_audio_thread)
    t.start()

def is_speaking():
    """Check if MIRA is currently talking"""
    return pygame.mixer.music.get_busy()

if __name__ == "__main__":
    say("System online. Audio output initialized.")