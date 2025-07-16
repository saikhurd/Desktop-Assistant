import speech_recognition as sr 
import webbrowser as web 
import pyttsx3
import datetime
import wikipedia
import subprocess
import os
import smtplib


print("Initializing alex")

MASTER = "sai"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#speak function will pronouce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("good morning" + MASTER)

    elif hour>=12 and hour<18: 
         speak("good afternoon" + MASTER)   

    else:
         speak("good Evening" + MASTER)

    speak("I am alex. how may i help you?")    


def takeCommand():

    path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("please say something...")
        audio = r.listen(source)
        #print("reconizing now...")
    
    try: 
        print("recognizeing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: P{query}\n")
       # dest = r.recognize_google(audio)
        #dest = r.recognize_google(audio)

       # print("you have said : " + dest)
       # web.get(path).open(dest)

    except Exception as e:
        print("Error : " + str(e))

    return query    

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia ")
            speak(results)
