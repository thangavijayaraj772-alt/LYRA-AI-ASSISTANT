import os
import ctypes
import pyautogui
from datetime import datetime
from speech import speak,listen
import shutil
def shutdown_pc():
    speak("Shutting down your computer.")
    os.system("shutdown /s /t 1")

def restart_pc():
    speak("Restarting your computer.")
    os.system("shutdown /r /t 1")

def lock_pc():
    speak("Locking your computer.")
    ctypes.windll.user32.LockWorkStation()

def take_screenshot():
    speak("do you ant to give name to this photo")
    query = listen()
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%I%M%S')}.png"
    if "i want" in query:
         speak("tell a name")
         filename_input = listen().strip().replace(" ","_")
         filename_input += ".png"
         filename = filename_input
    elif "no" in query or query is None:
      pass
    else:
       speak("i didn't catch that")
    folder = r"D:\4 Sight\OneDrive - 4sight RCM\Desktop\books\JARVIS screenshots"
    pyautogui.screenshot(filename)
    shutil.move(filename,folder)
    

    speak(f"Screenshot saved as {filename} in jarvis screenshot folder")
