import pyttsx3
import speech_recognition as sr 
import webbrowser
import datetime
import subprocess
import os
import time 

def sptext ():
    recoginzer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak NOW listening.....")
        recoginzer.adjust_for_ambient_noise(source)
        audio = recoginzer.listen(source)
        try:
            print("recognizing....")
            data = recoginzer.recognize_google(audio) 
            print (data)
            return data
        except sr.UnknownValueError:
            print("Not Understanding Voice ")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    if "siri" in sptext().lower():
            while True:
                data1=sptext().lower()
                if "your name" in data1:
                    name = "my name is siri,how can i help you "
                    speechtx(name)
                elif "open google" in data1:
                    webbrowser.open("https://www.google.com/")
                    speechtx("google opened")
                elif "open my linkedin" in data1:
                    webbrowser.open("https://www.linkedin.com/in/siddhant-singh59469/")
                    speechtx("linkedin opened")
                elif"open my instagram" in data1 :
                    webbrowser.open("https://www.instagram.com/")
                    speechtx("instagram opened")
                elif"open ai" in data1 :
                    webbrowser.open("https://chatgpt.com/")
                    speechtx("AI opened")
                elif"youtube" in data1:
                    webbrowser.open("https://www.youtube.com/")
                    speechtx("youtube opened")
                elif"time" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)
                elif"date" in data1:
                    date = datetime.datetime.now().strftime("%d/%m/%Y")
                    speechtx(date)
                elif'play song' in data1:
                    add ="C:\music"
                    listsong = os.listdir(add)
                    print(listsong)
                    os.startfile(os.path.join(add,listsong[0]))
                elif 'exit' in data1:
                    speechtx("Exiting")
                    break
                time.sleep(7)
    else:
        print("thank you")