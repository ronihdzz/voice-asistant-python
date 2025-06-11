# 🎙️ Voice AI Assistant con OpenAI Realtime API y Twilio

## Language / Idioma
- [English](README.md)
- **Español** (actual)

---

Un asistente de voz inteligente que combina la potencia de **OpenAI Realtime API** con **Twilio Voice** para crear conversaciones de voz en tiempo real. Este proyecto permite realizar llamadas telefónicas y tener conversaciones naturales con un asistente de IA.

> **Nota Importante**: Este proyecto está basado completamente en la documentación oficial de Twilio. He tomado el artículo base y creado un template más organizado y estructurado, pero el concepto y la implementación principal siguen fielmente el tutorial original de Twilio.

## 📖 Referencia Original

- **Artículo base**: [Voice AI Assistant with OpenAI Realtime API and Python](https://www.twilio.com/en-us/blog/voice-ai-assistant-openai-realtime-api-python)

Este proyecto es una reorganización  del código presentado en el artículo oficial de Twilio, manteniendo la misma funcionalidad pero con una estructura más modular y profesional.

## 🚀 ¿Qué hace este proyecto?

- **Recibir llamadas telefónicas** a través de Twilio Voice
- **Procesar audio en tiempo real** usando WebSockets
- **Generar respuestas inteligentes** con OpenAI GPT-4o Realtime API  
- **Responder con voz sintetizada** de vuelta al llamador
- **Mantener conversaciones naturales** con detección automática de voz

### Características principales:

- ✅ **Conversaciones de voz bidireccionales** en tiempo real
- ✅ **Detección automática de voz** (Voice Activity Detection)
- ✅ **Múltiples voces disponibles** (configurables)
- ✅ **Sistema de logging avanzado** con Loguru
- ✅ **Configuración por ambientes** (local, development, production)
- ✅ **Arquitectura modular** con FastAPI
- ✅ **Containerización** con Docker

## 🏗️ Arquitectura del Sistema

### Componentes principales:

1. **FastAPI Server** - Servidor web que maneja webhooks y WebSockets
2. **Twilio Voice** - Plataforma de telefonía que recibe las llamadas
3. **OpenAI Realtime API** - Motor de IA para procesamiento de voz
4. **WebSocket Bridge** - Puente bidireccional para streaming de audio

## 🔄 Flujo de Interacción y Webhooks

### Fases del Proceso:

#### 🟢 Fase 1: Establecimiento de Llamada 
1. El usuario llama al número de Twilio configurado
2. Twilio envía un webhook HTTP POST/GET a `/incoming-call`
3. El servidor responde con TwiML que incluye:
   - Mensaje de bienvenida (`<Say>`)
   - Instrucción de conexión WebSocket (`<Connect><Stream>`)

#### 🟡 Fase 2: Establecimiento de Conexiones WebSocket
1. Twilio conecta al WebSocket `/media-stream` del servidor
2. El servidor establece conexión con OpenAI Realtime API
3. Se envía configuración inicial (`session.update`) a OpenAI
4. OpenAI confirma la configuración (`session.updated`)

#### 🔵 Fase 3: Streaming de Audio Bidireccional
1. **Twilio → FastAPI**: Audio del usuario como eventos `media` (G.711 μ-law)
2. **FastAPI → OpenAI**: Audio convertido a base64 (`input_audio_buffer.append`)
3. **OpenAI → FastAPI**: Respuesta de IA como `response.audio.delta`
4. **FastAPI → Twilio**: Audio de respuesta procesado
5. **Twilio → Usuario**: Reproducción de la respuesta de IA

#### 🔴 Fase 4: Finalización 
1. El usuario cuelga la llamada
2. Twilio desconecta el WebSocket
3. El servidor cierra la conexión con OpenAI

## ⚙️ Configuración Técnica Detallada

### 🤖 Configuración OpenAI
```python
session_update = {
    "type": "session.update",
    "session": {
        "turn_detection": {"type": "server_vad"},     # Detección automática de voz
        "input_audio_format": "g711_ulaw",           # Formato de entrada
        "output_audio_format": "g711_ulaw",          # Formato de salida  
        "voice": "alloy",                            # Voz configurada
        "instructions": SYSTEM_MESSAGE,              # Prompt del asistente
        "modalities": ["text", "audio"],             # Modalidades soportadas
        "temperature": 0.8                           # Creatividad de respuestas
    }
}
```

### 🎯 Prompt del Sistema
```python
SYSTEM_MESSAGE = (
    "You are a helpful and bubbly AI assistant who loves to chat about "
    "anything the user is interested in and is prepared to offer them facts. " 
    "You have a penchant for dad jokes, owl jokes, and rickrolling – subtly. "
    "Always stay positive, but work in a joke when appropriate."
)
```

## 📁 Estructura del Proyecto

```
voice-assistant-python/
├── src/
│   ├── main.py                 # Servidor principal FastAPI
│   ├── prompts.py             # Prompts del sistema
│   └── core/
│       ├── settings/
│       │   ├── __init__.py    # Exportaciones de settings
│       │   └── base.py        # Configuraciones base
│       └── utils/
│           └── environment.py  # Manejo de ambientes
├── envs/                      # Variables de entorno por ambiente
├── pyproject.toml            # Configuración Poetry
├── requirements.txt          # Dependencias pip
├── docker-compose.yml        # Configuración Docker
├── Dockerfile.deploy         # Dockerfile de producción
└── README.md                # Este archivo
```

## 🔧 Tecnologías Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno y rápido
- **[WebSockets](https://websockets.readthedocs.io/)** - Comunicación bidireccional en tiempo real
- **[Twilio Voice API](https://www.twilio.com/docs/voice)** - Plataforma de telefonía
- **[OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime)** - IA conversacional en tiempo real
- **[Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)** - Manejo de configuraciones
- **[Loguru](https://loguru.readthedocs.io/)** - Sistema de logging avanzado
- **[Poetry](https://python-poetry.org/)** - Gestión de dependencias

## 🤝 Créditos y Reconocimientos

Este proyecto está **completamente basado** en el excelente tutorial de Twilio:

**"[Build a Voice AI Assistant with OpenAI's Realtime API and Python](https://www.twilio.com/en-us/blog/voice-ai-assistant-openai-realtime-api-python)"**

### ¿Qué aporta este repositorio?

- ✨ **Estructura modular y profesional** del código
- 🏗️ **Configuración por ambientes** (local, dev, prod)
- 🐳 **Containerización completa** con Docker
- 📝 **Documentación detallada** y diagramas
- 🔧 **Manejo de configuraciones** con Pydantic
- 📊 **Sistema de logging mejorado**
- 🎯 **Separación de responsabilidades**

## 📞 Funcionamiento 

1. **Usuario llama** al número de Twilio configurado
2. **Escucha el mensaje** de bienvenida
3. **Empieza a hablar** cuando se le indica
4. **Mantiene conversación** natural con el asistente
5. **Cuelga** cuando termina la conversación

El asistente puede hablar sobre cualquier tema, hacer chistes y mantener conversaciones naturales gracias a GPT-4o. 