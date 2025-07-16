import pyttsx3
import speech_recognition as sr
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("good morning" )

    elif hour>=12 and hour<18: 
         speak("good afternoon" )   

    else:
         speak("good Evening")

    speak("I am alex. how may i help you?")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("recognizeing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: P{query}\n")
       # dest = r.recognize_google(audio)
        #dest = r.recognize_google(audio)

       # print("you have said : " + dest)
       # web.get(path).open(dest)

    except Exception as e:
        #print(e)
        print("say that again...")
        return"None"
        
    return query
       
if __name__ == "__main__":
    wishMe()
    takeCommand()
