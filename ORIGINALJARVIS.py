import pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # --no-warn-script-location
import webbrowser
import pywhatkit
import pyjokes
import pyaudio
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    speak("I AM JARVIS  ")
    print("I AM JARVIS ")
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    elif hour >= 18 and hour < 0:
        speak("Good Evening")
        print("Good Evening")

    else:
        speak("It's time for going to bed, complete your work soon ")
        print("It's time for going to bed, complete your work soon ")

    speak(" Please tell me how may I help you")
    print(" please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

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
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'who is ' in query:
            speak('Searching Wikipedia...')
            print('searching wikipedia ...')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            print('searching wikipedia....')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia ")
            print(result)
            speak(result)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('youtube is going to open that song')
            speak('playing' + song)
            print('youtube opening')
            pywhatkit.playonyt(song)



        elif 'nothing' in query:
            print("THANK YOU")
            speak("thank you")

        elif 'google' in query:
            search = query.replace('search ', '')
            search = query.replace('google', '')
            speak('google is going to open')
            print('google opening')
            pywhatkit.search(search)




        # elif 'play music' in query:
        #     music_dir = 'G:\\kishan all.co\\d\\songs'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is ",{strTime})
            print("current time :", strTime)

        elif 'who created you'  in query:
            speak("DINESH KUMAR")
            print("DINESH KUMAR")

        elif 'groups ' in query:
            grp_id = input("enter group id:")
            message = input("enter a message:")
            time = input("enter the time in 24 hrs format:")
            minutes = input("enter time in minutes:")
            pywhatkit.sendwhatmsg_to_group(grp_id,message,time,minutes)







        elif 'single' in query:
            speak("no , i am in relationship with wifi")
            print("No , I am in Relationship with wifi")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'owner' in query:
            speak('my master  DHINESH')
            print("my master  DHINESHKUMAR .R")

        elif 'i love you' in query:
            speak("sorry i am already committed bro")
            print("sorry i am already committed bro")

        elif ' message ' in query:
            a = input("enter phone number")
            b = input("enter message")
            c = int(input("enter time in hour in 24 hrs format"))
            d = int(input("enter time in minutes "))
            pywhatkit.sendwhatmsg(a,b,c,d,)





        # elif 'open code' in query:
            # codePath = "C:\\Users\\kishancjx\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            # os.startfile(codePath)

        elif 'wish me' in query:
            wishme()
            # you should enter your path here

