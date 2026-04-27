import subprocess
from collections import deque
import os
from speech import speak,listen

Base = os.path.expanduser("~")

folders = {
    "desktop":os.path.join(Base,"Desktop"),
    "documents":os.path.join(Base,"Documents"),
    "downloads":os.path.join(Base,"Downloads")
}

def search_file(filename):
    queue = deque()
    for folder in folders.values():
        queue.append(folder)
    while queue:
        current_path = queue.popleft()
        try:
            for items in os.listdir(current_path):
                full_path = os.path.join(current_path,items)
                if os.path.isfile(full_path):
                    if filename.lower() in items.lower():
                     return full_path
                if os.path.isdir(full_path):
                    if filename.lower() in items.lower():
                        return full_path
                    queue.append(full_path)
        except Exception:
            continue
    return None

def open_file(filename):
    path = search_file(filename)
    if not path:
        speak("file not found")
        return
    print(f"opening:{path}")
    speak("opening your file")
    try:
        os.startfile(path)
    except Exception as e:
        print(e)
        speak("error opening file")