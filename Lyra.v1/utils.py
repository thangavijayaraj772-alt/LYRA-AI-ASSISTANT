from datetime import datetime
from speech import speak
import random

def greeting():
    hour = datetime.now().hour
    morning = [
        "Good morning, sir. Ready to begin?",
        "Morning, sir. Lyra is online.",
        "Good morning. What’s the plan today?"
    ]

    afternoon = [
        "Good afternoon, sir. How can I assist?",
        "Afternoon. I'm ready when you are.",
        "Good afternoon. What would you like to do?"
    ]

    evening = [
        "Good evening, sir. Ready for your commands.",
        "Evening. How can I help?",
        "Good evening. What’s next?"
    ]

    night = [
        "It's quite late, sir. Still working?",
        "Late hours, sir. I'm here if needed.",
        "You should get some rest sir... but I'm available."
    ]
    if 5 <= hour < 12:
        speak(random.choice(morning))
    elif 12 <= hour < 17:
        speak(random.choice(afternoon))
    elif 17 <= hour < 21:
        speak(random.choice(evening))
    else:
        speak(random.choice(night))

def time():
    time = datetime.now()
    current_time = time.strftime("%I:%M:%p")
    speak(f"the current time is{current_time}")
