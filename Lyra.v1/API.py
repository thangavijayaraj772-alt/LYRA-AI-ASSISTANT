import json
import tkinter as tk
from tkinter import messagebox
import os

CONFIG_FILE = "config.json"

def save_API(gemini_key,weather_key):
    
    data={
        "gemini_api":gemini_key,
        "weather_api":weather_key       
    }
    with open(CONFIG_FILE,"w") as f:
        json.dump(data,f,indent=4)
    
def old_data():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE,"r") as f:
            return json.load(f)
            
    return {}       
        
def open_window(): 
 def save_button(): 
   gemini_key=gemini_entry.get().strip()
   weather_key=weather_entry.get().strip()
   
   save_API(gemini_key,weather_key)  
   messagebox.showinfo("Success","API key saved successfully")
   root.destroy() 
   
 old=old_data()  
        
 root=tk.Tk()
 root.title("Lyra API")
 root.geometry("500x300")
 root.resizable(False,False)

 title=tk.Label(root,text="Enter your API keys",font=("Arial",16,"bold"))
 title.pack(pady=10)

 tk.Label(root,text="Gemini API key").pack()
 gemini_entry=tk.Entry(root,width=60)
 gemini_entry.pack(pady=5)
 gemini_entry.insert(0,old.get("gemini_api",""))

 tk.Label(root,text="Weather API key").pack()
 weather_entry=tk.Entry(root,width=60)
 weather_entry.pack(pady=5)
 weather_entry.insert(0,old.get("weather_api",""))


 save_btn = tk.Button(root,text="Save",width=20,command=save_button)
 save_btn.pack(pady=20)

 root.mainloop()        
        