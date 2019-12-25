import speech_recognition as sr
import subprocess
from weather import weather

r1 = sr.Recognizer()

def kill_process():
    subprocess.call(["killall", "chrome"])

def tasks(text):
    pikachu = text.split()[0]
    commmand = text.split()[1]
    content = text.replace((pikachu + " " + commmand + " "), '')
    pikachu = pikachu.lower()
    commmand = commmand.lower()

    if(pikachu == "pikachu"):
        if(commmand == "play"):
            kill_process()
            subprocess.Popen(["node", "player.js", content])
        if(commmand == "stop"):
            kill_process()
        if(commmand == "what's"):
            if(content == "the weather now"):
                weather()
                
                

while True:
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
