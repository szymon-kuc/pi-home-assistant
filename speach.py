import speech_recognition as sr
import subprocess

rl = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

while True:
    with sr.Microphone(device_index=0) as source:
        print('speak now')
        audio = r3.listen(source)

        try:
            get = r3.recognize_google(audio)
            print(get)
            txt = ""
            if(len(get.split()) > 2):
                txt = get.split()[0] + " " + get.split()[1]
                get = get.replace(txt + " ", '')
                txt = txt.lower()
            if(txt == "pikachu play"):
                subprocess.Popen(["killall", "chrome"])
                subprocess.Popen(["node", "bot.js", get])
            if(get == "stop"):
                subprocess.Popen(["killall", "chrome"])
        except sr.UnknownValueError as e:
            print(e)
        except sr.RequestError as e:
            print(format(e))