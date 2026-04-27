from google import genai
from speech import speak,listen
import os
from API import CONFIG_FILE
import json

history=[]

def saved_key():
  if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE,"r") as f:
        config=json.load(f)
        return config.get("gemini_api","")
  return ""

def ask_gemini(prompt):
    try:
        if not prompt.strip():
         return "Empty input received"
        api = saved_key() 
        if not api:
            speak("gemini api is not added")
            return "No api key"
                 
        os.environ["GOOGLE_API_KEY"]=api
        client=genai.Client()
        
        history.append(f"user:{prompt}")
        
        context = "\n".join(history[-6:])
        
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=context
        )
        reply = response.text
        history.append(f"Ai:{reply}")
        return reply
    except Exception as e:
        print("your gemini quota exceeded,please wait and try again")
        speak("your gemini quota exceeded,please wait and try again")
        return "gemini is unavailable now"
def reasoning_mode():
    speak("tell me your complex probelm")
    query = listen()
    reasoning_prompt = f"""you are a reasoning engine.Analyze the problem step by step and give a clear solution.probelm : {query}"""
    result = ask_gemini(reasoning_prompt)
    print(result)
    speak(result)
    