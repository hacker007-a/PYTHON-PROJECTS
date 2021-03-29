import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def chat(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        chat('playing' + song)
        pywhatkit.playonyt(song)
    if 'search' in command:
        sear = command.replace("search", '')
        chat('searching' + sear)
        pywhatkit.search(sear)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        chat('Current time is ' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,5 )
        print(info)
        chat(info)
    elif 'joke' in command:
        chat(pyjokes.get_joke())
    else:
        chat("Please say again")


while True:
    run_jarvis()