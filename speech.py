import speech_recognition as sr
import subprocess
import time
from weather import weather_commands
from yt import play
import os
from gtts import gTTS 

r1 = sr.Recognizer()

def voice():
    with sr.Microphone() as source:
        print('speak now')
        audio = r1.listen(source)
        try:
            get = r1.recognize_google(audio)
            print(get)
            if(len(get.split()) >= 2):
                tasks(get)    
        except sr.UnknownValueError as e:
            print(e)
        except sr.RequestError as e:
            print(format(e))

def speech(answer):
        speech = gTTS(text = answer, lang = 'en', slow = False)
        speech.save("text.mp3")
        os.system("mpg123 text.mp3")

def kill_process():
    subprocess.call(["killall", "brave"])

def tasks(text):
    pikachu = text.split()[0]
    command = text.split()[1]
    content = text.replace((pikachu + " " + command + " "), '')
    pikachu = pikachu.lower()
    command = command.lower()

    if(pikachu == "pikachu"):
        if(command == "play"):
            kill_process()
            play(content)
        elif(command == "stop"):
            kill_process()
        elif("weather" in content):
            weather_commands(content)
        elif(command == "how" or command == "when" or command == "who" or command == "where" or "lyrics" in content or (command == "what" and "weather" not in content)):
            kill_process()
            subprocess.call(["node", "google_search.js", (command + " " + content)])
            f = open("Output.txt", "r")
            speech(f.read())
        else :
            speech("Sorry, I don't understand that")

time.sleep(1)

while 1:
    voice()
    
