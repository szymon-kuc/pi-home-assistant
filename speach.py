import speech_recognition as sr
import subprocess

rl = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

def kill_process():
    subprocess.Popen(["killall", "chrome"])

def tasks(text):
    pikachu = text.split()[0]
    commmand = text.split()[1]
    content = text.replace((pikachu + " " + commmand + " "), '')
    pikachu = pikachu.lower()
    commmand = commmand.lower()

    if(pikachu == "pikachu"):
        if(commmand == "play"):
            kill_process()
            subprocess.Popen(["node", "bot.js", content])
        if(commmand == "stop"):
            kill_process()

while True:
    with sr.Microphone() as source:
        print('speak now')
        audio = r3.listen(source)
        try:
            get = r3.recognize_google(audio)
            print(get)
            if(len(get.split()) >= 2):
                tasks(get)    
        except sr.UnknownValueError as e:
            print(e)
        except sr.RequestError as e:
            print(format(e))
