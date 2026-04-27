# save infof
from speech import speak,listen
import json
import os

FILE = "personal.json"
def load_personal_info():
  if os.path.exists(FILE):
   try:
    with open(FILE,"r") as f:
      return json.load(f)
   except json.JSONDecodeError:
     return {}
  return {}

def save_personal_info(data):
    with open(FILE,"w") as f:
        json.dump(data,f,indent=4)

personal_info = load_personal_info()


def personal():
  speak("what i want to say")
  q = listen().lower()
  for key,value in personal_info.items():
    if q in key.lower() or key in q:
      speak(f"your {key} is {value}")
      return
  speak("I don't have any information")
    
    
def store_the_info():
  speak("say the information")
  speak("what is your key sir")
  key = listen().lower()
  print(key)
  speak(f"your key is {key}")
  speak("now say the value")
  value = listen().lower()
  print(value)
  speak(f"your value for the {key} is {value}")
  speak("should i save this information")
  text=listen().lower()
  if "save" in text or "ok" in text or "yes" in text or "safe" in text or "i want" in text:
    personal_info[key] = value
    save_personal_info(personal_info)
    speak(f"got it, sir. i saved your {key} as {value}.")
  else:
    speak("this information is not saved")
  print(personal_info)
  
  
  
  



