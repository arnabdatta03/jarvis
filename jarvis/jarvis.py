import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
                  speak("Good Afternoon!")   

            
    else:
        speak("Good Evening Sir!")

    speak("I am jarvis. Please tell me how may I  help you")
def takecommand():   
    #it takes microphone input from the users and return string output

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.puse_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
       # print(e)
        print("Say  again please...")
        return "None"
    return query
    
if __name__ == "__main__":
    #speak("Arnab is a good boy")
    wishMe()
    while True:
     query = takecommand().lower()
    #loogic for excuting task based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=1)
        speak("According to wikipedia")
        print(result)
        speak(result)
        

