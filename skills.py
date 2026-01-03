import os
import webbrowser
import pyautogui
import time
from AppOpener import open as app_open

def open_website(site_name):
    """Opens a site and waits a bit for it to load"""
    site_name = site_name.lower().replace(" ", "")
    url = f"https://www.{site_name}.com"
    webbrowser.open(url)
    time.sleep(2) 
    return f"Opening {site_name}."

def search_in_active_window(query, current_app="browser"):
    """Types into the current search bar"""
   
    if current_app == "spotify":
        pyautogui.hotkey('ctrl', 'l')
    else:
        pyautogui.press('/') 
    
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    
    pyautogui.write(query, interval=0.05)
    pyautogui.press('enter')
    return f"Searching for {query}."

def open_app(app_name):
    """
    Opens apps with specific fixes for Windows Store Apps (WhatsApp/Spotify)
    """
    app_name = app_name.lower()
    
    try:
        
        if "whatsapp" in app_name:
            os.system("start whatsapp:")
            time.sleep(3)
            return "Opening WhatsApp."
            
       
        elif "spotify" in app_name:
            os.system("start spotify:")
            time.sleep(3)
            return "Opening Spotify."

       
        else:
            app_open(app_name, match_closest=True, output=False)
            time.sleep(3) 
            return f"Opening {app_name}."
            
    except Exception as e:
        print(f"[Skills Error] {e}")
        return f"I couldn't open {app_name}."


def play_media():
    pyautogui.press('playpause')
    return "Toggling playback."

def skip_song():
    pyautogui.press('nexttrack')
    return "Skipping track."

# Whats app er malpati and unnoto logic, whatsapp re rape kore open korar jnno
def draft_whatsapp_msg(contact_name, message):
    
    os.system("start whatsapp:")
    time.sleep(3) 
    
   
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(1)
    
    
    pyautogui.write(contact_name)
    time.sleep(1.5) 
    pyautogui.press('enter') 
    time.sleep(1)
    
  
    pyautogui.write(message, interval=0.05)
    
    return f"Drafted message to {contact_name}. Say 'Send' to confirm."

def send_message():
    pyautogui.press('enter')
    return "Message sent."


def close_window():
    pyautogui.hotkey('alt', 'f4')
    return "Closing window."

def switch_tab():
    pyautogui.hotkey('ctrl', 'tab')
    return "Switching tab."