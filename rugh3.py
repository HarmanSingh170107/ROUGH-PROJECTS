import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=='__main__':
        speak("Initialising Jarvis.............. ")