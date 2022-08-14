import pyttsx3      #text to speech module. -> used to convert the text to speech.
import datetime     #datetime module. -> used to get date and time.
import speech_recognition as sr #speech to text module. -> used to convert the speech to text.
import wikipedia    #to search content in wikipedia.
import smtplib      #Sending email to give email.
import webbrowser as wb     #Seach directly in chrome.
import os           #Used to control the log out, shut down and restart.
import pyautogui    #Used to take screenshot and records.
import psutil       #Used to get CPU status.
import pyjokes      #Used to get jokes.

engine = pyttsx3.init()
engine.setProperty('voice', 'english_rp+f4')
engine.setProperty('rate', 135)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("Today's date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning Yuvaraj.")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Yuvaraj.")

    elif hour >= 18 and hour < 24:
        speak("Good Evening Yuvaraj.")

    else:
        speak("Good Night Yuvaraj.")

    speak("Welcome back sir, This is Zara.")
    speak("How can I help you sir?")

def wiki():
    speak("Please wait...")
    print("Searching...")
    queries = ""
    queries = queries.replace("wikipedia", "")
    result = wikipedia.summary(f'{query}', sentences=2)
    print(result)
    speak(result)

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("cs205114663@bhc.edu.in", "8778048590")
    server.sendmail("yuvarajrama121@gmail.com", to, content)
    server.close()

def searchInChrome():
    speak("What should I search for?")
    chromePath = "/usr/bin/google-chrome %s"
    search = takeCommand().lower()
    wb.get(chromePath).open_new_tab(search + ".com")

def shutDown():
    speak("Are You sure to shutdown?")
    confirm = takeCommand()
    if confirm == 'yes':
        os.system('systemctl poweroff')
    else:
        speak("Continue")
        exit()

def restart():
    speak("Are You sure to restart?")
    confirm = takeCommand()
    if confirm == 'yes':
        os.system('systemctl restart')
    else:
        speak("Continue")

def rememberThat():
    speak("What should I have to remember?")
    data = takeCommand()
    speak("You said me to remember" + data)
    remember = open("data.txt", "w")
    remember.write(data)
    remember.close()

def screenShot():
    img = pyautogui.screenshot()
    img.save("hhh.jpg")

def cpu():
    usage = str(psutil.cpu_percent())
    print(usage)
    speak("CPU is at " + usage)

    battery = psutil.sensors_battery()
    print(battery)
    speak("battery is at ")
    speak(battery.percent)

def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)


def takeCommand():
    r = sr.Recognizer()          
    with sr.Microphone() as source:      
        print("Listening...")
        audio = r.record(source, duration=4)
        try:
            print("Recognizing...")
            str=r.recognize_google(audio)
            print(str)
        except:
            print("Some error has been occurred!")

            return ""
        return str

if __name__ == "__main__":

    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            wiki()

        elif "email" in query:
            try:
                speak("What shoud I have to say?")
                content = takeCommand()
                to = "yuvarajrama121@gmail.com"
                sendMail(to, content)
                speak("Email has been sent successfulluy!")
            except Exception as e:
                print(e)
                speak("Unable to send the message.")

        elif "search in chrome" in query:
            searchInChrome()

        elif "shutdown" in query:
            shutDown()

        elif "restart" in query:
            restart()
        
        elif "remember that" in query:
            rememberThat()

        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that" +remember.read())

        elif "screenshot" in query:
            screenShot()
            speak("Screen Shot has been caputured and stored.")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()

        elif "offline" in query:
            speak("Have a happy vibe.")
            quit()

        else:
            speak("Try again")
            print("Try again!!")
