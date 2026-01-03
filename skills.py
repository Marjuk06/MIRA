import os
import webbrowser
import datetime
import pyautogui
import time
from AppOpener import open as app_open

# --- BROWSER CONTROLS ---
def open_website(site_name):
    """Opens a site and waits a bit for it to load"""
    site_name = site_name.lower().replace(" ", "")
    url = f"https://www.{site_name}.com"
    webbrowser.open(url)
    time.sleep(2) # Wait for page to load
    return f"Opening {site_name}."

def search_in_active_window(query):
    """Types into the current search bar (YouTube/Google/Spotify)"""
    # 1. Click the search bar (YouTube/Google uses '/')
    pyautogui.press('/') 
    time.sleep(0.5)
    
    # 2. Clear previous text (Ctrl+A, Backspace)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    
    # 3. Type and Enter
    pyautogui.write(query, interval=0.05)
    pyautogui.press('enter')
    return f"Searching for {query} here."

# --- APP CONTROLS ---
def open_app(app_name):
    try:
        app_open(app_name, match_closest=True, output=False)
        time.sleep(3) # Wait for app to open
        return f"Opening {app_name}."
    except:
        return f"Could not find {app_name}."

# --- MEDIA CONTROLS (Spotify/YouTube) ---
def play_media():
    pyautogui.press('playpause') # Hits the global Play/Pause key
    return "Toggling playback."

def skip_song():
    pyautogui.press('nexttrack')
    return "Skipping track."

# --- WHATSAPP AGENT ---
def draft_whatsapp_msg(contact_name, message):
    # 1. Open WhatsApp (assuming installed app or pinned tab)
    app_open("whatsapp", match_closest=True, output=False)
    time.sleep(3) # Wait for it to pop up
    
    # 2. Search for Contact (Ctrl + F)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.5)
    pyautogui.write(contact_name)
    time.sleep(1)
    pyautogui.press('enter') # Select contact
    
    # 3. Type Message but DO NOT SEND
    time.sleep(0.5)
    pyautogui.write(message, interval=0.05)
    
    return f"I have typed the message to {contact_name}. Say 'Send it' to confirm."

def send_message():
    pyautogui.press('enter')
    return "Message sent."

# --- WINDOW CONTROLS ---
def close_window():
    pyautogui.hotkey('alt', 'f4')
    return "Closing window."

def switch_tab():
    pyautogui.hotkey('ctrl', 'tab')
    return "Switching tab."