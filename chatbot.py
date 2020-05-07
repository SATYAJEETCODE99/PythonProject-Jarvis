import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os
import random
import sys
import scrapingurl
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<=17:
        speak("Good Afternoon Sir")
    else :
        speak("Good Evening Sir")

    speak("starseed here Please tell me sir how may i help you")

def takeC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.../")
        #r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing your voice.....")
        query = r.recognize_google(audio)
        print(f"You said {query}\n")
        
    except Exception:
        speak("Say that again please")
        return "None"
    return query
def sendfunc(to,content):
    server = smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('satyajeet_majumdar@gmail.com','')
    server.sendmail('satyajeet_majumdar@gmail.com',to,content)
    server.close()
def closeLappy():
    os.system("shutdown /s /t 1")
def restartLappy():
    os.system("shutdown /r /t 1")
def randomHi():
    li = ['hey','ho','yep','hola','bonjour','salut','Guten tag','Salve','Konnichiwa' ]
    random.shuffle(li)
    speak(random.choice(li))
def jokes():
    lijokes = ["Doctor: I'm sorry but you suffer from a terminal illness and have only 10 to live. Patient: What do you mean, 10? 10 what? Months? Weeks?!Doctor: Nine.","My old aunts would come and tease me at weddings, Well Sarah? Do you think you’ll be next?We’ve settled this quickly once I’ve started doing the same to them at funerals.","An old grandma brings a bus driver a bag of peanuts every day.First the bus driver enjoyed the peanuts but after a week of eating them he asked: Please granny, don't bring me peanuts anymore. Have them yourself.The granny answers: You know, I don't have teeth anymore. I just prefer to suck the chocolate around them."]
    random.shuffle(lijokes)
    speak(random.choice(lijokes))

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeC().lower()
        if 'wikipedia' in query:
            speak("Searching in Wikipedia sir please wait")
            if "wikipedia" in query or "search" in query or "in" in query or "about" in query or "all" in query or "information" in query:
                query = query.replace("wikipedia"," ")
                query = query.replace("search"," ")
                query = query.replace("in"," ")
                query = query.replace("about"," ")
                query = query.replace("all"," ")
                query = query.replace("information"," ")
            results=wikipedia.summary(query,sentences=8)
            speak("According to wikipedia it says...")
            speak(results)
        elif 'youtube' in query:
            query = query.replace("youtube","")
            query = "youtube.com/"+query
            webbrowser.open(query)
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif 'quit' in query:
            speak("Do you really want to quit") 
            query = takeC().lower()
            if 'yes' in query:
                speak("Okay sir shutting down the system")
                sys.exit(0)
            else:
                speak("Okay") 
        elif 'email' in query:
            try:
                speak("What should I send sir")
                content = takeC()
                to = "satyajeet_majumdar@gmail.com"
                sendfunc(to,content)
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry sir the email cannot be sent at this moment")
        if query == 'shutdown my laptop' or query =='shutdown my computer':
            speak("Do you really want to shut down your computer say yes or no")
            query = takeC().lower()
            if query == 'yes':
                closeLappy()
            else:
                speak("Thank You sir waiting for your next command")
        elif query == 'restart my laptop' or query == 'restart my computer':
            speak("Do you really want to restart your computer say yes or no")
            query = takeC().lower()
            if query == 'yes':
                restartLappy()
            else:
                speak("Computer will not be restarted")

        if query == 'hi' or query == 'hello' or query == 'hey' or query == 'ho':
            randomHi()
        elif 'weather' in query or 'temperature' in query:
            speak(scrapingurl.main())
        elif 'jokes' in query or 'joke' in query:
            jokes()


                