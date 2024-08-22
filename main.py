import pyttsx3
import datetime
import distutils
import wikipedia
import webbrowser
import os
import random
#import smtplib
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis ,Sir, How can I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=0.8
        audio=r.listen(source)

    try:
        print("Recongnizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query



if __name__=="__main__":
    wishMe()
    #while True:
    if 2:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir='C:\\Music'
            songs=os.listdir(music_dir)
            random_song=random.choice(songs)
            print(f"Now Playing: {random_song}")
            os.startfile(os.path.join(music_dir, random_song))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The Time is: {strTime}")
            print(f"Sir, The Time is: {strTime}")

    
        else:
            speak('Sorry Sir Can you Repeat please')