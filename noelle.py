import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import pyaudio
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am noelle. how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('danielashulamithjustin@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()

    
    chrome_path = "C://Program Files//Google//Chrome//Application//Chrome.exe %s"
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.get(chrome_path).open("google.com")

        elif 'open stack overflow' in query:
            speak("opening stack overflow")
            webbrowser.get(chrome_path).open("stackoverflow.com") 

        elif 'open reddit' in query:
            speak("opening reddit")
            webbrowser.get(chrome_path).open("reddit.com")  

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")
        
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query:
            speak("I was created by Daniela.")
        
        elif "what is your favourite colour" in query or "your favourite colour" in query:
            speak("I like all shades of blue")

        elif "do you have a boyfriend" in query:
            speak("I'm in love with the wifi")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Daniela")

        elif 'open spotify' in query:
            for r, d, f in os.walk('c:\\'):
                for file in f:
                    if file.endswith("Spotify.exe"):
                        path_file = os.path.join(r,file)
                        codePath = path_file.replace('\\', '\\\\')
                       
            os.startfile(codePath)

        elif 'open discord' in query:
            for r, d, f in os.walk('c:\\'):
                for file in f:
                    if file.endswith("Discord.exe"):
                        path_file = os.path.join(r,file)
                        codePath = path_file.replace('\\', '\\\\')

            os.startfile(codePath)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            for r, d, f in os.walk('c:\\'):
                for file in f:
                    if file.endswith("Code.exe"):
                        path_file = os.path.join(r,file)
                        codePath = path_file.replace('\\', '\\\\')

            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "danielashulamithjustin@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")    
