import pyttsx3
import speech_recognition as sr
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=5)
       
    try:
        print("recongizing...")
        query=r.recognize_google(audio,language='en-in')
        #audio = r.listen(source)
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"

if __name__ == "__main__":
   speak("hello sir")