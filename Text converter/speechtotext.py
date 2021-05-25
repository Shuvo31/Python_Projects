import pyttsx3
import speech_recognition
def get():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Say Something ...")
        audio=r.listen(source)
        print("Done!")
    try:
        text=r.recognize_google(audio)
        print("You said"+ text)
    except Exception as e:
        print(e)

get()
