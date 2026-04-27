import pyttsx3
import speech_recognition as sr
import time
 


def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',140)
    recognizer  = sr.Recognizer()
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.3)
  


def listen():
        recognizer  = sr.Recognizer()
        with sr.Microphone() as source:
          recognizer.adjust_for_ambient_noise(source, duration=0.2)
          audio = recognizer.listen(source)
        try:
          return recognizer.recognize_google(audio, language="en-US").lower()
         
        except:
          return ""

  