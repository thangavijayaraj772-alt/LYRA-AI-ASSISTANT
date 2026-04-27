import speech_recognition as sr
from speech import speak
from utils import greeting

recognizer = sr.Recognizer()

def listen_for_wake_word(jarvis):
    """Continuously listen for the wake word."""
    with sr.Microphone() as source:
        print("Listening for wake word...")
        while True:
            try:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                text = recognizer.recognize_google(audio, language="en-US").lower()
                print("Heard:", text)
                if "lyra" in text:
                    print("yes sir!")
                    return True
            except sr.WaitTimeoutError:
                # Timeout, just continue listening
                continue
            except Exception:
                print(f"Error")
                continue
