from http import server
from re import search
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import requests
import sys
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password')
    server.sendmail('your email id',to,content)
    server.close()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am jarvis. Please tell me how  I can help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("do you have any other work sir...")   
        print("do you have any other work sir...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube...')
        elif 'thanks' in query or 'thank you' in query:
            speak("its my pleasure,sir")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak('opening facebook...')
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak('opening instagram...')
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak('opening whatsapp...')
        elif 'open makaut' in query:
            webbrowser.open("https://makaut1.ucanapply.com/smartexam/public/")
        
            speak('opening makaut...')
        elif 'open telegram' in query:
            webbrowser.open("https://web.telegram.org/k/")
        
            speak('opening telegram...')
        elif 'open hub' in query:
            webbrowser.open("https://github.com/arnabdatta03/arnabdatta03/new/main?filename=README.md&path=%2F&value=-+%F0%9F%91%8B+Hi%2C+I%E2%80%99m+%40arnabdatta03%0A-+%F0%9F%91%80+I%E2%80%99m+interested+in+...%0A-+%F0%9F%8C%B1+I%E2%80%99m+currently+learning+...%0A-+%F0%9F%92%9E%EF%B8%8F+I%E2%80%99m+looking+to+collaborate+on+...%0A-+%F0%9F%93%AB+How+to+reach+me+...%0A%0A%3C%21---%0Aarnabdatta03%2Farnabdatta03+is+a+%E2%9C%A8+special+%E2%9C%A8+repository+because+its+%60README.md%60+%28this+file%29+appears+on+your+GitHub+profile.%0AYou+can+click+the+Preview+link+to+take+a+look+at+your+changes.%0A---%3E%0A")
            speak('opening hub...')
        elif 'tata' in query:
            webbrowser.open("https://g01.tcsion.com/LX/login#l")
            speak('opening tata...')
        elif 'open mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm#inbox")
            speak('opening mail...')
        elif 'who make you' in query:
            speak('arnab sir,make me and he is my boss')

        elif 'open google' in query:
            #speak("sir, what should i search on google")
            #cm = takeCommand().lower
            webbrowser.open("google.com")
            speak('opening google...')
        elif 'play video on youtube' in query:
            speak("sir, what should i search on youtube")
            cm = takeCommand().lower
            webbrowser.open(f"{cm}")

        #elif 'open stack' in query:
           # webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = "C:\\Users\\arnabdatta\\Desktop\\Music"
            songs = os.listdir(music_dir)
            speak('playing music...')
            rd = random.choice(songs)
            print(songs)    
            os.startfile(os.path.join(music_dir, rd))
        
       
        elif 'you need break' in query:
            
            
        
            speak(" ok sir,you can call me anytime,have a good day.")
            sys.exit()

            #speak("sir,do you have any other work") 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

       
        elif "open notepad" in query:
            npath = "C:\\Users\\arnabdatta\\Documents\\jarvis.txt"
            os.startfile(npath)
            speak('opening notepad...')
        elif "open command" in query:
            npath = "C:\\Users\\arnabdatta\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            os.startfile(npath)
            speak('opening command...')
        elif "ip address" in query:
            ip= get('https://api.ipify.org').text
            #print(e)
            speak(f"sir your IP address is{ip}")
            

        

        elif 'email to alex' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower
                to = "arnab112datta@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend arnab bhai. I am not able to send this email")
        #else:
            search = 'https://www.google.com/search?q='+query #bujhta na parle direct google a search kora daba
            webbrowser.open(search)
           
        