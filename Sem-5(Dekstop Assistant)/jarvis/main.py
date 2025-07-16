import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
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

#this function will wish you as per the time
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

#this command will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please") 
        query = None   

    return query    

# main program starts here    
speak("Initializing alex...")  
wishMe() 
query = takeCommand()

#logic for executing tasks as per query
if 'wikipedia' in query.lower():
    speak('searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)

#elif 'open youtube' in query.lower():
    #webbrowser.open("youtube.com")
   # url = "youtube.com"
    #chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
   # webbrowser.get(using='google-chrome').open(url,new=2)

    #chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    #webbrowser.get(chrome_path).open(url)
    #urL = 'https://www.google.com'
    #chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    #webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
    #webbrowser.get('chrome').open_new_tab(urL)
    # Open a page with Chrome through Python
 
#import webbrowser
#chromedir= 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s'
#webbrowser.get(chromedir).open("https://pythonprogramming.altervista.org/wp-admin")

#webbrowser.get('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s')open_new("https://google.com")
#def main():

    
    #path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    #r = sr.Recognizer()
    #with sr.Microphone() as source:
     #   r.adjust_for_ambient_noise(source)
      #  print("please say something ")
       # audio = r.listen(source)
        #print("reconizing now...")

        #try:
         #   dest = r.recognize_google(audio)
          #  print("you have said : " + dest)
           # webbrowser.get(path).open(dest)

       # except Exception as e:
        #    print("Error : " + str(e))

#if __name__ == "__main__":
 #   main()
# import webbrowser

#url='https://www.mozilla.org'
#webbrowser.register('firefox', None)
#webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
#webbrowser.get('firefox').open(url)


