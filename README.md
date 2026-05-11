# JARVIS AI Desktop Assistant

A fully voice-controlled AI desktop assistant inspired by Iron Man’s JARVIS, built using Python, PyQt5, Speech Recognition, and Neural Text-to-Speech.

This project transforms the desktop into a live AI assistant interface with:
- continuous rotating HUD
- wake-word activation
- voice conversations
- intelligent command routing
- smart web/app launching
- conversational AI integration

---

# Features

## AI HUD Interface
- Transparent desktop HUD overlay
- Continuous rotating circular JARVIS core
- Frameless wallpaper-style interface
- Real-time state transitions
- Dynamic opacity changes
- Listening/thinking/speaking animations
- Pulse breathing effect while listening

---

# Voice Assistant System

## Wake Word Detection
Supports:
- "Jarvis"
- "Hey Jarvis"
- "OK Jarvis"

The assistant stays in passive standby until activated.

---

## Continuous Voice Interaction
After activation:
- continuously listens for commands
- executes tasks
- replies with neural voice responses

No keyboard interaction required.

---

# Neural AI Voice

Implemented using:
- Coqui TTS
- VCTK neural voice models

Features:
- realistic neural speech
- natural male AI voice
- dynamic speech generation
- offline voice synthesis

---

# Speech Recognition

Implemented using:
- SpeechRecognition
- Google Speech API

Includes:
- microphone calibration
- wake-word recognition
- continuous command listening
- ambient noise tuning

---

# Intelligent Command Routing

The assistant can understand:
- open commands
- launch commands
- search requests
- conversational phrasing
- shutdown commands

Examples:
- "Open YouTube"
- "Launch Spotify"
- "Can you open WhatsApp"
- "Watch Interstellar trailer"
- "Find AI tutorials"
- "Search Amazon for gaming mouse"

---

# Smart Application Launcher

Supports:
- desktop applications
- websites
- intelligent search routing

Examples:
- Chrome
- VS Code
- WhatsApp
- Spotify
- Telegram
- Discord
- Gmail
- LinkedIn
- YouTube
- Netflix

---

# Intelligent Search System

Automatically routes searches to:
- Google
- YouTube
- Spotify
- Amazon

Examples:
- "Watch Interstellar trailer"
- "Play Arijit Singh"
- "Search Amazon for headphones"
- "What is Quantum Computing?"

---

# Conversational AI Integration

Integrated with OpenAI API.

JARVIS can:
- answer generic questions
- explain concepts
- hold conversations
- provide intelligent responses
- act as a conversational AI assistant

Examples:
- "Who was Oppenheimer?"
- "Explain black holes"
- "How do neural networks work?"
- "What is quantum computing?"

---

# Technologies Used

## Frontend / UI
- PyQt5
- QGraphicsScene
- QGraphicsSvgItem
- SVG HUD Rendering

## AI / Voice
- OpenAI API
- Coqui TTS
- SpeechRecognition

## Backend
- Python
- Multithreading
- Subprocess
- Webbrowser

---

# Project Structure

```text
JARVIS/
│
├── core/
│   ├── ai_engine.py
│   ├── command_router.py
│   ├── response_engine.py
│   └── state_manager.py
│
├── system/
│   ├── app_controller.py
│   └── voice_engine.py
│
├── ui/
│   └── hud.py
│
├── states/
│   └── jarvis_states.py
│
├── main.py
├── jarvis_core_master.svg
└── README.md
```

---

# State System

JARVIS operates using multiple internal states:

| State | Description |
|---|---|
| OFF | Waiting for wake word |
| LISTENING | Listening for commands |
| THINKING | Processing request |
| EXECUTING | Running commands |
| SPEAKING | Voice response mode |
| IDLE | Awaiting next interaction |

---

# Current Capabilities

## Voice Control
- Wake-word activation
- Continuous listening
- Voice command execution
- Conversational AI responses

## Desktop Control
- Open applications
- Open websites
- Smart searches
- Browser automation initiation

## AI Features
- GPT-powered responses
- Natural language understanding
- Intent-based routing

---

# Future Roadmap

## Planned Features
- Memory system
- File system access
- Desktop automation
- Email sending
- WhatsApp automation
- Spotify playback control
- System monitoring
- CPU/RAM diagnostics
- Face recognition
- Real wallpaper embedding
- Fully autonomous task execution

## Advanced AI Features
- Long-term memory
- Personalized behavior
- Vision-based interaction
- Offline LLM integration
- Autonomous reasoning

---

# Installation

## Clone Repository

```bash
git clone <your-repo-link>
cd JARVIS
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install pyqt5
pip install SpeechRecognition
pip install pyaudio
pip install sounddevice
pip install soundfile
pip install TTS
pip install openai
```

---

# Run JARVIS

```bash
python main.py
```

---

# Example Usage

```text
Hey Jarvis

Open YouTube

Play phonk music

Who was Oppenheimer?

Search Amazon for gaming mouse

Shutdown
```

---

# Inspiration

Inspired by:
- Iron Man's JARVIS
- futuristic AI assistants
- holographic HUD systems
- autonomous desktop agents

---

# Author

Kshitij Shukla

AI Desktop Assistant Project