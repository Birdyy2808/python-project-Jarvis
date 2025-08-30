Jarvis Voice Assistant

A Python-based virtual voice assistant that can open websites, play music, fetch news, and respond to general queries using OpenAI GPT.

✨ FEATURES:

    🎤 Voice command recognition using SpeechRecognition

    🔊 Text-to-speech response using pyttsx3

    🌐 Open websites like Google, YouTube, GitHub, LinkedIn

    🎵 Play songs from a predefined music library

    📰 Open Google News

    🤖 AI-powered responses via OpenAI API

🛠️ TECH STACK:

    🐍 Python 3.x

    🗣️ SpeechRecognition

    🎙️ PyAudio

    🔊 pyttsx3

    🤖 OpenAI

⚙️ CONFIGURATION:
Set your OpenAI API key:

For Windows (PowerShell):
Command: $Env:OPENAI_API_KEY="your_api_key_here"

For macOS/Linux:
Command: export OPENAI_API_KEY="your_api_key_here"

▶️ RUN THE ASSISTANT:
Command: python main.py

Say "Jarvis" to wake the assistant, then give a command such as:

open google

open github

play <song-name>

news

exit (to stop Jarvis)
