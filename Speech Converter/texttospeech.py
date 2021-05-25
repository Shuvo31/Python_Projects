import pyttsx3
speech=input("Enter the text which u need to convert:\n") #user input
engine=pyttsx3.init()
#engine.say("Hi! My name is Shuvojit Das. I am a competitive programmer.")
engine.say(speech)
engine.runAndWait()