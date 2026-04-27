import os
from my_personal_info import personal_info
from speech import speak


MEMORY_FILE = "memory.txt"
store_info = "storedinfo.txt"
def remember(text):
    text=text.strip()
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE,"r") as f:
            notes=[n.strip() for n in f.readlines()]
        if text in notes:
            return "I already remember it"
    with open(MEMORY_FILE, "a") as f:
        f.write(text + "\n")
    return "Got it,I will remember that"

def recall(keyword=None):
    if not os.path.exists(MEMORY_FILE):
        return "I don't remember anything yet"
    
    with open(MEMORY_FILE, "r") as f:
        notes = f.readlines()
    
    if keyword:
        filtered = [n.strip() for n in notes if keyword.lower() in n.lower()]
        if filtered:
            return "I remember: "+", ".join(filtered)
        else:
            return "I couldn't find anything related"
    
    
    return "You asked me to remember: " + ", ".join([n.strip() for n in notes])
    

def print_info():
    print(personal_info)
    try:
     with open(store_info,"w") as f:
        for keys,values in personal_info.items():
          f.write(f"{keys}:{values}\n")
     speak("Your info is printed")
    except Exception as e:
        speak("something went wrong")
        
def clear_memory():
    if os.path.exists(MEMORY_FILE):
            open(MEMORY_FILE,"w").close()
            return "memory cleared"
    return "NO memory to clear"


         