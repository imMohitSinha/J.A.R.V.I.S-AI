import pyttsx3 # pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib


print("Initializing Jarvis")

MASTER = "Sir"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak function will pronounce the string which is passed to it 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    print(hour)


    if hour >= 0 and hour <12:
        speak("Good Morning" + MASTER )
    elif hour >= 12 and hour < 18: 
        speak("Good Afternoon" + MASTER )
    else: 
        speak("Good Evening" + MASTER )
    
    #speak("I am jarvis. How may I help you sir?")

def takeCommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        audio = r.listen(source)
    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")



    except Exception as e: 
        print("Say that again please")
        query = None
    return query

def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail("pt1282241@gmail.com", to, content)
    server.close()


# Main Program starts here....

def main(): 


    #speak("Initializing Jarvis...")
    wishMe()
    query = takeCommand()



    # Logic for executing tasks as per the query

    if 'wikipedia' in query.lower(): 
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        #webbrowser.open("youtube.com")

        url= "youtube.com"
        chrome_path = 'C:/Program Files/Google/Chrome/Application/Chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open reddit' in query.lower():
        #webbrowser.open("youtube.com")

        url= "reddit.com"
        chrome_path = 'C:/Program Files/Google/Chrome/Application/Chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\Asus\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[1]))

    elif 'the time' in query.lower():

        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query.lower():
        codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to mohit' in query.lower():
        try: 
            speak("What should I send")
            content = takeCommand()
            to = "pt1282241@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent successfully")
        except Exception as e: 
            print(e)

main()







































































































































































































