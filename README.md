# 🤖 LYRA - Learning Your Responsive Assistant

LYRA is a voice-controlled AI assistant inspired by JARVIS.  
It can understand voice commands, perform system tasks, and respond intelligently using AI.

---

## ✨ Features

- 🎤 Voice Input & Output  
- 🤖 AI-powered responses (Gemini API)  
- 📂 Open software and files using voice  
- 🌐 Weather information  
- 🧠 Memory system (remember & recall)  
- ⚙️ System controls (shutdown, restart, screenshot)  
- 🔑 API setup GUI  

---

## 🧠 What does LYRA mean?

**LYRA = Learning Your Responsive Assistant**

A personalized AI assistant that learns from the user and responds intelligently in real time.

---

## 🗣️ Commands Guide

Below are example voice commands you can use with LYRA.

---

### 🔹 Activation

"Lyra"  
→ Wakes up the assistant and starts listening  

---

### 🔹 Basic Interaction

"What is the time?"  
→ Tells current system time  

---

### 🔹 AI / Knowledge (Gemini)

"Tell me about Artificial Intelligence"  
→ AI-generated explanation  

"What is Python?"  
→ Answers general questions  

---

### 🔹 File & Application Control

"Open <software name>"  
→ Opens apps (Chrome, YouTube, Notepad, etc.)

"<name> file open"  
→ Searches and opens a file  

"<folder name> file open"  
→ Opens folders like Desktop, Downloads  

"Close <software name>"  
→ Closes the software  

---

### 🔹 System Control

"Shutdown system" → Shuts down PC  
"Restart system" → Restarts PC  
"Take screenshot" → Captures screen  

---

### 🔹 Memory System

"Remember this..."  
→ Stores memory  

"Recall <keyword>"  
→ Retrieves stored memory  

"Store information"  
→ Saves key-value data with confirmation  

---

### 🔹 Search & Information

"Information about <topic>"  
→ Fetches summary from Wikipedia  

"What is the weather?"  
→ Provides weather update  

---

## 🔑 API Setup

⚠️ API keys are required for full functionality.

LYRA uses external APIs for AI responses and weather data.

---

### 1️⃣ Gemini API (AI Responses)

1. Go to Google AI Studio  
2. Generate an API key  
3. Copy the key  

---

### 2️⃣ Weather API

1. Go to https://openweathermap.org  
2. Generate an API key  
3. Copy the key  

---

### ⚙️ Add API Keys in LYRA

After starting LYRA, say:

"API setup" or "settings"  

→ A window will open  
→ Enter your Gemini & Weather API keys  

---

## 🎯 Command Tips

- Speak clearly  
- Use simple phrases  
- Start with "Lyra"  
- Commands support natural language  

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/LYRA-AI-Assistant.git
cd LYRA-AI-Assistant
pip install -r requirements.txt
python lyra.py
