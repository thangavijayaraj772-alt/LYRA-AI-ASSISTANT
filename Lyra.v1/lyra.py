#for voice input and output
from speech import speak, listen
from wake import listen_for_wake_word
#Information modules
from weather import get_weather
from wikipedia_info import get_info
#AI module
from gemini_ai import ask_gemini,reasoning_mode,history
#control modules
from software_control import open_software, close_software
from system_control import shutdown_pc, restart_pc, lock_pc, take_screenshot
#memory module
from memory import remember, recall,print_info,clear_memory
#utility module
from utils import greeting,time
#cities module
from cities import states_of_india
#file handling module
from files import open_file
#personal info module
from my_personal_info import personal, store_the_info,personal_info
#GUI window for api 
from API import old_data,open_window

import webbrowser
import requests
from bs4 import BeautifulSoup

def basic_commands(command,weather_key):
    # basic commands
             
        if "weather" in command:
         if weather_key:
            speak("Which city?")
            city = listen()
            speak(get_weather(city))
         else:
            speak("please fill your API")
         return True
                    
        elif "time" in command:
            time()
            return True
        
        elif "api setup" in command or "settings" in command:
            open_window()
            config=old_data()
            gemini_key = config.get("gemini_api","")
            weather_key=config.get("weather_api","")
    
            speak("api setup successfully changed")
            return config
                    
        elif "shutdown" in command:
            shutdown_pc()
            return True
                    
        elif "restart" in command:
            restart_pc()
            return True
                    
        elif "lock" in command:
            lock_pc()
            return True
                    
        elif "screenshot" in command:
            take_screenshot()
            return True
                
        elif "lyra" in command:
            speak("Yes Sir!")
            return True
                    
        elif "goodbye" in command or "exit" in command:
            speak("Goodbye sir.")
            return 'exit'  # exit the program
                
        elif "sleep" in command or "go back to wake word" in command:  # new: go back to wake mode
            speak("Going back to sleep. Say 'Jarvis' to wake me up again.")
            return 'sleep'  # break inner loop -> listen for wake word again
        return False
    

def personalinfo_command(command):
    # personal info
        if "say my name" in command:
            if "name" in personal_info:
                speak(personal_info["name"])
                        
            else:
                speak("doesn't stored")
            return True
        elif "reset my profile" in command:
            personal_info.clear()
            speak("your personal information is cleared")
            return True
                     
        elif "my info" in command:
            personal()
            return True
                    
        elif "store information" in command:
            store_the_info()
            return True
                    
        elif "say my birthday" in command:
            speak(personal_info["birthday"])
            return True
                
        elif "who is kavin" in command:
            speak("he is my boss's favourite boy")
            return True

        elif "say my favourite boy name" in command:
            speak("kavin indrajith")
            return True
        return False
             
def online_information(command):
    # information from online
        if "information about" in command:
            topic = command.replace("information about", "").strip()
            speak(get_info(topic))
            return True
                    
               
def AI_commands(command):                  
             # AI commands    
        if command.lower().startswith("tell me about"):
            text = command.replace("tell me about", "").strip()
            speak(ask_gemini(text))
            return True
                 
        elif "question" in command:
            speak("What is your question?")
            q = listen()
            speak(ask_gemini(q))
            return True
                    
        elif "problem" in command:
            reasoning_mode()
            return True
        return False

def media_command(command):
    # media command
        if "play video" in command:
            speak("What do you want me to play?")
            query = listen()
            if not query:
                speak("I didn't hear anything. Please try again.")
                return True
                    
            print(f"Searching YouTube for: {query}")

                 # YouTube search URL
            url = f"https://www.youtube.com/results?search_query={query}"
            html = requests.get(url).text

                 # Extract first video link from HTML
            start_index = html.find("/watch?v=")
            if start_index == -1:
                speak("Sorry, I couldn't find any video.")
                return True
                      

            end_index = html.find('"', start_index)
            video_path = html[start_index:end_index]
            video_url = "https://www.youtube.com" + video_path

            print(f"Opening video: {video_url}")
            speak(f"Playing {query} on YouTube")
            webbrowser.open(video_url)  
            return True
                    
        elif "search video" in command:
            speak("what to search")
            query = listen()
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            return True
        return False
    
def software_command(command):
    #software command
        if command.startswith("open "):
            software = command.replace("open", "").strip()
            open_software(software)
            return True
                    
        elif command.startswith("close "):
            software = command.replace("close", "").strip()
            close_software(software)
            return  True
        return False
             
def files_command(command):
    # files and memory    
        if "file open"in command:
            filename = command.replace("file open","").strip()
            print(filename)
            if not filename:
                speak("which file should i open?")
                filename=listen()
            if not filename:
                speak("i didn't hear anything")
                return True
            speak(f"searching for {filename}")
            open_file(filename)
            return True
            
        
        elif "print info" in command:
            print_info()
            return True
                 
        
        elif "delete memory" in command:
            speak(clear_memory())
            return True
            
        
        elif "clear chat" in command:
            history.clear()
            speak("memory cleared")
            

        elif "remember" in command:
            text = command.replace("remember", "").strip()
            remember(text)
            speak("I will remember that.")
            return True

        elif "recall" in command:
            keyword=command.replace("recall","").strip()
            if keyword:
             speak(recall(keyword))
            else:
                speak(recall())
            return True
        return False
             
def unknown_command(command):
        speak(f"should i say about {command}")
        reply = listen()
        print(reply)
        if 'tell me' in reply:
            speak(ask_gemini(command))
        else:
            speak("okay sir")
        return True
    
                
    

    
    
def main():
    config = old_data()
    
    gemini_key=config.get("gemini_api","")
    weather_key=config.get("weather_api","")
    
    
    speak("lyra is online. Say 'lyra' to activate me.")
    
    while True:
        # Wait for wake word
        if listen_for_wake_word("lyra"):
            greeting()
            
            while True:
                command = listen().lower()
                if not command:
                    continue
                try:
                   
                   result = basic_commands(command,weather_key)
                   if isinstance(result,dict):
                       config=result
                       gemini_key=config.get("gemini_api","")
                       weather_key=config.get("weather_api","")
                       
                       continue
                   
                   if result == 'sleep':
                         break
                   elif result == 'exit':
                           return
                   elif result:
                       continue
                   
                   
                   if personalinfo_command(command):
                       continue
                   
                   if online_information(command):
                       continue
                   
                   if AI_commands(command):
                       continue
                   
                   if media_command(command):
                       continue
                   
                   if software_command(command):
                       continue
                   
                   if files_command(command):
                       continue
                    
                   if unknown_command(command):
                       continue
                except Exception as e:
                    print(e)
                    speak("something went wrong,please check the program")
if __name__ == "__main__":
    main()

