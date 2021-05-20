import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import wolframalpha
import os
import smtplib
import sys
import requests 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
client = wolframalpha.Client('VUU4A6-L779YEJ2AY')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour <=18:
        speak("Good Afternoon! ")
    else:
        speak("Good Evening!")
    speak('starting all system applications')
    speak('installing all drivers')
    speak('every driver is installed')
    speak('all systems have been started')
    speak("Hello Nishan   sir. Please tell me how may i help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e: 
        speak("sir say that again please")
        print("say that again please......")
        return "None"
    return query
    
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nishan.timilsina@apexcollege.edu.np','nissant10')
    server.sendmail('nishan.timilsina@apexcollege.edu.np',to,content)
    server.close()
def findReceiver(name):
    contacts = {"Nissant": "ntimilsina07@gmail.com",
                "class": "enum@apexcollege.edu.np"}
    try:
        receiverGmail = contacts[name]
        return receiverGmail
    except:
        return 0

def givenews():
    apiKey = '468928361e4143bcaacabea4b2b9f9ef'
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=468928361e4143bcaacabea4b2b9f9ef  "
    r = requests.get(url)
    data = r.json()
    data = data["articles"]
    flag = True
    count = 0
    for items in data:
        count += 1
        if count > 10:
            break
        print(items["title"])
        to_speak = items["title"].split(" - ")[0]
        if flag:
            speak("Today's top ten Headline are : ")
            flag = False
        else:
            speak("Next news :")
        speak(to_speak)


if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak('opening youtube sir')
            webbrowser.open("youtube.com")

            
        elif 'open google' in query:
             speak('opening google sir')
             webbrowser.open("google.com")
        elif 'open facebook' in query:
             speak('opening facebook sir')
             webbrowser.open("facebook.com")
        elif 'play my best music' in query:
            speak("ok sir enjoy")
            music_dir='C:\\Users\\Nissant\\Downloads\\my song'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is{strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\Nissant\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)
        elif 'email to' in query or 'send a mail' in query or 'mail to' in query:
            receiver = query.split(" ")[len(query.split(" "))-1]
            to = findReceiver(receiver)
            if to != 0:
                try:
                    speak("What is your message ?")
                    content = takeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry sir, something went wrong and i am not able to send your email right now.")
       

        elif 'how are you' in query:
            speak("i am fine sir what about you sir")      
        elif 'fine' in query:
            speak("how can i help you sir")
        elif 'hello jarvis' in query:
            speak("hello sir")       
        elif'who are you' in query:
            speak("i am your assitant")
        elif 'who develop you' in query or'who made you' in query:
            speak("Nissant Timilsina develop me")
        elif 'headline' in query or 'news' in query or 'today headline' in query:
            givenews()

















        elif 'bye  jarvis' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()  
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
        else:
            query == query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)
                    print(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak(results)
                    print(results)
        
            except:
                webbrowser.open('www.google.com')

        
            
       
       







       