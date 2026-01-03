import asyncio
import edge_tts
import pygame
import os

# Voice Options:
# "en-US-AriaNeural" -> Energetic, American Female (Great for Jarvis style)
# "en-GB-SoniaNeural" -> British Female (Polite, smooth)
# "en-US-GuyNeural" -> Male (If you want a male Jarvis)
VOICE = "en-US-AriaNeural"

async def speak(text):
    # 1. Generate the audio file
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("response.mp3")

    # 2. Initialize the audio player
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    
    # 3. Play the audio
    print("M.I.R.A. is speaking...")
    pygame.mixer.music.play()

    # 4. Wait for audio to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # 5. Clean up (release the file so we can delete/overwrite it later)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    
    # Optional: Delete the file after playing
    # os.remove("response.mp3")

# Wrapper to run the async function easily from other files
def say(text):
    asyncio.run(speak(text))

if __name__ == "__main__":
    say("System online. Audio output initialized. Ready for commands, Marjuk.")