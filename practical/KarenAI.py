import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishme():
    hour= int(datetime.datetime.now().hour)


def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone as source:
            print('listening...')
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print('recognising')
            query = r.recognize_google(audio, language='en-in')
            print(f'user said: {query}\n')

        except Exception as e:
            print('say again')
            return 'none'
        return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('google.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M')
            speak(f'Sir, the time is {strTime}')

        # elif'play music' in query:
        #     music_dir = 'C:\\Users\\Ashu\\Downloads\\dl'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))




                