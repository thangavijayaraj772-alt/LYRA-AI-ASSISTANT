import subprocess
import os
from speech import speak
import webbrowser

def open_software(name):
    if 'chrome' in name:
        speak('Opening Chrome...')
        subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
    elif 'edge' in name:
        speak('Opening Microsoft Edge...')
        subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"])
    elif 'notepad' in name:
        speak('Opening Notepad...')
        subprocess.Popen(['notepad.exe'])
    elif 'calculator' in name:
        speak('Opening Calculator...')
        subprocess.Popen(['calc.exe']) 
    elif "youtube" in name:
        speak('opening youtube')
        webbrowser.open(f"https://www.youtube.com")
    elif "instagram" in name:
        speak("opening instagram")
        webbrowser.open(f"https://www.instagram.com/")
    elif "chat gpt" in name:
        speak("openning chat gpt")
        webbrowser.open(f"https://chatgpt.com/")
    
    elif "whatsapp" in name:
        speak("opening whatsapp")
        webbrowser.open(f"https://web.whatsapp.com/")

    else:
        speak(f"I couldn't find {name}")
    

def close_software(name):
    if 'chrome' in name:
        os.system("taskkill /f /im chrome.exe")
    elif 'edge' in name:
        os.system("taskkill /f /im msedge.exe")
    elif 'notepad' in name:
        os.system("taskkill /f /im notepad.exe")
    elif 'youtube' in name:
        speak('closing youtube')
        os.system("taskkill /im chrome.exe /f") 
    elif 'instagram' in name:
        speak("closing instagram")
        os.system("taskkill /im chrome.exe /f")
    elif 'calculator' in name:
        os.system("taskkill /f /im CalculatorApp.exe")
    elif 'whatsapp' in name:
        os.system("taskkill /im chrome.exe /f")
    elif 'chat gpt' in name:
        os.system("taskkill /im chrome.exe")

    else:
        speak(f"No running software named {name}")
