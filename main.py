import datetime
import speech_recognition as sr
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)  # voice of david


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    ''' Greeting according to the time'''
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

    print("I am your Assistant. How can I help you?")
    speak("I am your Assistant. How can I help you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
         print("Recognizing...")
         query = r.recognize_google(audio, language='en-in')
         print("User said:", query)

        except Exception as e:
         print("Can't understand..Say that again ")
         speak("Can't understand..Say that again. Please")
         return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('1941012609.k.harshvardhan@gmail.com', 'srkmsd0207')
    server.sendmail('1941012609.k.harshvardhan@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    greetMe()

    #logics for task
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)


        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open maps' in query:
            webbrowser.open("maps.google.com")
        elif 'order food' in query:
            webbrowser.open("zomato.com")
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'F:\\My song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
            print(strTime)
        elif 'open discord' in query:
            discord_path = 'C:\\Users\\user\\AppData\\Local\\Discord\\Update.exe'
            os.startfile(discord_path)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vardhanharsh15900@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, I can't be sent")









