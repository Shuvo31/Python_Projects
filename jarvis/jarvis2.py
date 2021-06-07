import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("Welcome back !")
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    speak(f"The current time is:{Time}")
#time()

def wiki():
    query=("Android (robot)")
    results=wikipedia.summary(query, sentences=2)
    speak("According to wikipedia")
    print(results)
    speak(results)

#wiki()

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to your words...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, Language="en-in")
        print(f"You said:{query}")
    except Exception as e:
        print(e)
        print("Say it again...")
        speak("Say it again..")
        return "None"
    return query
command()    