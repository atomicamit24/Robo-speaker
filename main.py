import pyttsx3

print("Welcome to Robospeaker 1.1. Created by Amit inspired by Harry")

engine = pyttsx3.init()
engine.setProperty('rate', 150)     # Speed of speech
engine.setProperty('volume', 0.8)   # Volume (0.0 to 1.0)

while True:
    x = input("Enter what you want me to say (or 'q' to quit): ")
    if x == "q":
        engine.say("Bye bye friend")
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()
