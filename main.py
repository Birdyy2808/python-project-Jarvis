import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
from openai import OpenAI
import os


def speak(text):
    engine = pyttsx3.init() # This is initializing the pytt
    # pyttsx3 is used to convert text to speech
    engine.say(text)
    engine.runAndWait()

def ai_process(command):
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def process_command(c):
    if "google" in c.lower():
        webbrowser.open("https://google.com")
    elif "github" in c.lower():
        webbrowser.open("https://github.com/Birdyy2808")     
    elif "linkedin" in c.lower():
        webbrowser.open("https://linkedin.com/")
    elif "youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        webbrowser.open("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN%3Aen")
    elif "exit" in c.lower() or "stop" in c.lower() or "quit" in c.lower():
        speak("Goodbye!")
        return False

    # Let OpenAI handle the requests
    else:
        output = ai_process(c)
        speak(output)

    return True



if __name__=="__main__":

    speak("Initializing Jarvis...")

    while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from microphone
        recognizer  = sr.Recognizer() # This will recognize what ever we speak
        

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
            word = recognizer.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("yes....")
                # listen for command
                with sr.Microphone() as source:
                    print("Awaiting command...")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                    command = recognizer.recognize_google(audio)
                    
                    if not process_command(command):
                        break

        except Exception as e:
            print("Error;{0}",format(e))
