import pyttsx3
import speech_recognition as srr
import datetime
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
time()
