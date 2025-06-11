# 🎙️ Voice AI Assistant with OpenAI Realtime API and Twilio

## Language / Idioma
- **English** (current)
- [Español](README.es.md)

---

An intelligent voice assistant that combines the power of **OpenAI Realtime API** with **Twilio Voice** to create real-time voice conversations. This project allows you to make phone calls and have natural conversations with an AI assistant.

> **Important Note**: This project is completely based on official Twilio documentation. I took the base article and created a more organized and structured template, but the concept and main implementation faithfully follow the original Twilio tutorial.

## 📖 Original Reference

- **Base Article**: [Voice AI Assistant with OpenAI Realtime API and Python](https://www.twilio.com/en-us/blog/voice-ai-assistant-openai-realtime-api-python)

This project is a reorganization of the code presented in the official Twilio article, maintaining the same functionality but with a more modular and professional structure.

## 🚀 What does this project do?

- **Receive phone calls** through Twilio Voice
- **Process real-time audio** using WebSockets
- **Generate intelligent responses** with OpenAI GPT-4o Realtime API  
- **Respond with synthesized voice** back to the caller
- **Maintain natural conversations** with automatic voice detection

### Main Features:

- ✅ **Bidirectional voice conversations** in real-time
- ✅ **Automatic voice detection** (Voice Activity Detection)
- ✅ **Multiple available voices** (configurable)
- ✅ **Advanced logging system** with Loguru
- ✅ **Environment configuration** (local, development, production)
- ✅ **Modular architecture** with FastAPI
- ✅ **Containerization** with Docker

## 🏗️ System Architecture

### Main Components:

1. **FastAPI Server** - Web server that handles webhooks and WebSockets
2. **Twilio Voice** - Telephony platform that receives calls
3. **OpenAI Realtime API** - AI engine for voice processing
4. **WebSocket Bridge** - Bidirectional bridge for audio streaming

## 🔄 Interaction Flow and Webhooks

### Process Phases:

#### 🟢 Phase 1: Call Establishment 
1. User calls the configured Twilio number
2. Twilio sends an HTTP POST/GET webhook to `/incoming-call`
3. Server responds with TwiML that includes:
   - Welcome message (`<Say>`)
   - WebSocket connection instruction (`<Connect><Stream>`)

#### 🟡 Phase 2: WebSocket Connection Establishment
1. Twilio connects to the server's `/media-stream` WebSocket
2. Server establishes connection with OpenAI Realtime API
3. Initial configuration (`session.update`) is sent to OpenAI
4. OpenAI confirms the configuration (`session.updated`)

#### 🔵 Phase 3: Bidirectional Audio Streaming
1. **Twilio → FastAPI**: User audio as `media` events (G.711 μ-law)
2. **FastAPI → OpenAI**: Audio converted to base64 (`input_audio_buffer.append`)
3. **OpenAI → FastAPI**: AI response as `response.audio.delta`
4. **FastAPI → Twilio**: Processed response audio
5. **Twilio → User**: AI response playback

#### 🔴 Phase 4: Termination 
1. User hangs up the call
2. Twilio disconnects the WebSocket
3. Server closes connection with OpenAI

## ⚙️ Detailed Technical Configuration

### 🤖 OpenAI Configuration
```python
session_update = {
    "type": "session.update",
    "session": {
        "turn_detection": {"type": "server_vad"},     # Automatic voice detection
        "input_audio_format": "g711_ulaw",           # Input format
        "output_audio_format": "g711_ulaw",          # Output format  
        "voice": "alloy",                            # Configured voice
        "instructions": SYSTEM_MESSAGE,              # Assistant prompt
        "modalities": ["text", "audio"],             # Supported modalities
        "temperature": 0.8                           # Response creativity
    }
}
```

### 🎯 System Prompt
```python
SYSTEM_MESSAGE = (
    "You are a helpful and bubbly AI assistant who loves to chat about "
    "anything the user is interested in and is prepared to offer them facts. " 
    "You have a penchant for dad jokes, owl jokes, and rickrolling – subtly. "
    "Always stay positive, but work in a joke when appropriate."
)
```

## 📁 Project Structure

```
voice-assistant-python/
├── src/
│   ├── main.py                 # Main FastAPI server
│   ├── prompts.py             # System prompts
│   └── core/
│       ├── settings/
│       │   ├── __init__.py    # Settings exports
│       │   └── base.py        # Base configurations
│       └── utils/
│           └── environment.py  # Environment handling
├── envs/                      # Environment variables by environment
├── pyproject.toml            # Poetry configuration
├── requirements.txt          # pip dependencies
├── docker-compose.yml        # Docker configuration
├── Dockerfile.deploy         # Production Dockerfile
└── README.md                # This file
```

## 🔧 Technologies Used

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern and fast web framework
- **[WebSockets](https://websockets.readthedocs.io/)** - Real-time bidirectional communication
- **[Twilio Voice API](https://www.twilio.com/docs/voice)** - Telephony platform
- **[OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime)** - Real-time conversational AI
- **[Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)** - Configuration management
- **[Loguru](https://loguru.readthedocs.io/)** - Advanced logging system
- **[Poetry](https://python-poetry.org/)** - Dependency management

## 🤝 Credits and Acknowledgments

This project is **completely based** on the excellent Twilio tutorial:

**"[Build a Voice AI Assistant with OpenAI's Realtime API and Python](https://www.twilio.com/en-us/blog/voice-ai-assistant-openai-realtime-api-python)"**

### What does this repository contribute?

- ✨ **Modular and professional structure** of the code
- 🏗️ **Environment configuration** (local, dev, prod)
- 🐳 **Complete containerization** with Docker
- 📝 **Detailed documentation** and diagrams
- 🔧 **Configuration management** with Pydantic
- 📊 **Improved logging system**
- 🎯 **Separation of responsibilities**

## 📞 How it Works 

1. **User calls** the configured Twilio number
2. **Listens to the welcome** message
3. **Starts talking** when indicated
4. **Maintains natural conversation** with the assistant
5. **Hangs up** when the conversation ends

The assistant can talk about any topic, make jokes and maintain natural conversations thanks to GPT-4o.

