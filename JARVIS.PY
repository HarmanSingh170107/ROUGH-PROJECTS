#pip install pyttsx3
import pyttsx3
import datetime
import time
import speech_recognition as sr
from termcolor import colored # allow text to get colored just write colored after rint and enclosed in brackets before text
from art import text2art
#pip install speechrecognition
#pip install pyttsx3
#pip install setuptools
#pip install pocketsphinx
#pip install termcolor pyfiglet
#pip install art
import webbrowser
import MusicLibrary
import requests # pip install requests
import ollama


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
r=sr.Recognizer()

newsapi='d3bafaf6fbf24d079c6942c3dfe7b445'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def datetime1():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Evening")

def Processcommand(c):
    sites=[['google',"https.//google.com"],
           ['youtube',"https.//youtube.com"],
           ['linkedin',"https.//linkedin.com"],
           ['wikipedia',"https.//wikipedia.com"]]
    for site in sites:
        if f"open {site[0]}" in c.lower():
            speak (f"opening {site[0]} as you asked for..............sir!")
            webbrowser.open(site[1])
        
    if c.lower().startswith("play"):
        try:
            song=c.lower().split(" ")[1]
            l=MusicLibrary.music[song]
            webbrowser.open(l)
        except KeyError:
            speak("Sorry, I couldn't find the song in your library.")
    elif 'news' in c.lower():
        response=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}",timeout=15)
        if response.status_code == 200:
        # Parse the JSON response
            data = response.json()
        # Extract the articles
            articles=data.get('articles',[])

        #Speak the headlines
            for article in articles:
                speak(article['title'])
        # strftime is a method used in Python to format datetime objects into strings according to a specified format.
        # The name stands for "string format time."
        # This method is part of the datetime module and allows you to convert datetime objects into human-readable strings by specifying a format using directives.

    elif "time" in c.lower():
        t=time.localtime()
        formatted_time= time.strftime("%H:%M:%S",t)
        print(formatted_time)
        speak(formatted_time)
    elif "date" in c.lower():
        t=time.localtime()
        formatted_date= time.strftime("%d/%m/%Y",t)
        print(formatted_date)
        speak(formatted_date)
    elif 'chat' in c.lower():
        
def microphone():
    
    if __name__=='__main__':
        speak("Initialising Jarvis..............")
        print(colored("Initialising Jarvis.............. ","light_yellow"))
        while True:
            r=sr.Recognizer()
            a=(colored("Recognizing", "light_red"))
            print (colored(a))
            
            try:
                with sr.Microphone() as source:
                    print("Listening")
                    audio=r.listen(source,timeout=3,phrase_time_limit=10)
                command=r.recognize_google(audio)

                if command.lower()=='jarvis':
                    print ('Initialized')
                    print(colored("Jarvis Active","light_blue"))
                    speak(f"{datetime1()}! How can I assist you today?")
                    print(command)
                    with sr.Microphone() as source:
            
                        audio=r.listen(source,timeout=3,phrase_time_limit=10)
                        command1=r.recognize_google(audio)
                        print(command1)
                        Processcommand(command1)
            
            except sr.UnknownValueError:
                print("Google could not understand audio")
            
            except sr.RequestError as e:
                print("Google error; {0}".format(e))
            
            except sr.WaitTimeoutError:
                print("Listening timed out. Please try again.")

microphone()

def chat():
    speak("Now what do you want to ask from me?")
    # Initialize the chat stream with a specific model
    stream = ollama.chat(model="mistral",messages=[{"role":"user","content":"What is the capital of France?"}])

    # Debug: Print the type and content of the stream object
    print("Stream type:", type(stream))
    print("Stream content:", stream)
