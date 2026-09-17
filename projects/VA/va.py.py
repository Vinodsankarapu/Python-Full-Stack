from gtts import gTTS
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import os


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("ika modhalupedadhama")
        audio = r.listen(source,phrase_time_limit = 10)
    data = " "
    try:
        data = r.recognize_google(audio)
        print("you said:",data)
    except sr.UnknownValueError as e:
        print("request failed")
    except sr.RequestError as e:
        print("speak clearly request is failing")
    return data
    #tts = gTTS(data)
    #tts.save("new.mp3")
    #playsound.playsound("new.mp3")
#listen()

def respond(string):
    """function to respond back"""
    print(string)
    tts = gTTS(string)
    tts.save("speech.mp3")
    filename = "speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def va(data):
    """our virtual assistant with the actions"""
    if "how are you" in data:
        listening = True
        respond("you bloody ediot go and study")
    elif "who is your favourite actor" in data:
        listening = True
        respond("i am very big fan of you")
    elif "what are your plans" in data:
        listening = True
        respond("nothing want to have fun with you")
    elif "stop talking" in data:
        listening = False
        respond("cool cool... chaduvuko velli")
    try:
        return listening
    except UnboundLocalError as e:
        print("make sure to speak louder")

respond(" rohit haa na frienduuu...")
listening = True
while listening:
    data = listen()
    listening = va(data)
