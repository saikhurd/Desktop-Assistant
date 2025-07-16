import os, sys
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

t = Translator()
r = sr.Recognizer()

if __name__ == "__main__":
    speak("हैलो मेरा नाम है। बताइये में आपकी क्या मदद कर सक्ती हूं")
    while True:
        with sr.Microphone() as source:
            speak("आपकी आवाज सुनी जा रही है")
            print("Listening your voice....")
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio, language='hi-IN')
                speak("आपने कहा: " + command)
                translated = t.translate(command, dest='en').text
                if "youtube" in translated.lower():
                    speak("youtube.com खोला जा रहा है")
                    print("Opening Youtube.com....")
                    webbrowser.open("https://www.youtube.com/")
                elif "wikipedia" in translated.lower():
                    speak("विकिपीडिया खोला जा रहा है")
                    print("Opening Wikipedia....")
                    webbrowser.open("https://wikipedia.org/")
                elif "discord" in translated.lower():
                    speak("discord खोला जा रहा है")
                    print("Opening Discord....")
                    os.startfile("C:/Users/Kunal/AppData/Local/Discord/Update.exe")
                elif "close" in translated.lower():
                    speak("प्रोग्राम बंद किया जा रहा है")
                    print("Stopping Program....")
                    sys.exit()
            except sr.UnknownValueError:
                speak("में आपकी आवाज समझ नहीं पा रहा हूं। कृपा फिर से बोलिए")
                print("Unrecognized Voice. Say that again please.")