# GenAI Medico Chatbot

GenAI Medico Chatbot is a multimodal AI healthcare assistant that combines voice and image understanding to provide preliminary medical guidance. Users can describe their symptoms through speech, upload an image, and receive an AI-generated medical response through an interactive Gradio interface.

---

## Features

- Voice-based symptom input
- Medical image analysis
- Speech-to-text using Groq Whisper
- AI-powered medical response generation
- Text-to-speech response using ElevenLabs
- Interactive Gradio interface
- End-to-end multimodal workflow

---

## Architecture

```
            User
      (Voice + Image)
             │
             ▼
      Speech-to-Text
       (Groq Whisper)
             │
             ▼
      Vision + Symptoms
             │
             ▼
      LLM Medical Analysis
             │
             ▼
      Doctor Response
             │
             ▼
      Text-to-Speech
       (ElevenLabs)
             │
             ▼
        Audio Response
```

---

## Tech Stack

- Python
- Gradio
- Groq API
- Whisper Large v3
- Llama Vision Model
- ElevenLabs
- Pillow
- SpeechRecognition
- gTTS
- python-dotenv

---

## Project Structure

```
genai-medico-chatbot/

├── brain_of_doctor.py
├── voice_of_the_patient.py
├── voice_of_the_doctor.py
├── gradio_app.py
├── requirements.txt
├── Pipfile
├── Pipfile.lock
├── .env
└── README.md
```

---

## Example Workflow

1. Upload a medical image.
2. Record your symptoms using the microphone.
3. Convert speech into text.
4. AI analyzes both the image and symptoms.
5. Receive a medical response.
6. Generate voice output for the response.

---

## Current Features

- Voice input
- Image input
- Speech-to-text transcription
- AI medical diagnosis
- Interactive Gradio interface

---

## Current Limitation

Doctor voice output is currently under improvement. Text responses are fully functional, while audio response generation is being refined.

---

## Future Improvements

- Better voice synthesis
- Conversation history
- Medical report generation
- PDF report export
- Support for multiple languages
- Better UI/UX
- RAG-based medical knowledge
- Gemini Vision support

---
