# from weatherApi import getWeather

import pyttsx3 #this module is responsible for speeaking
import speech_recognition as sr
import datetime
import os
import sys
import cv2
import random
import requests
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import pyautogui
from newsApi import*
from bitcoinPrice import*
from vaccination import getVaccine
import psutil
from whatsupMessage import*

engine = pyttsx3.init('sapi5') #this will be used in our speak function which will convert text into speach
voices = engine.getProperty('voices')
# print(voices[0].id)Gives us two options to use voices one male voice other female
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',170)

# this function conterts (text into speach)
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#this function take commands from user and converts into text (Voice to text)
def takeCommand():
    r = sr.Recognizer()
    '''
    Takes input speech from user
    takes input from microphone and returns string output
    '''
    with sr.Microphone() as source:
        print('Listening')
        # r.pause_threshold = 1
        audio = r.listen(source,timeout=3,phrase_time_limit=10)
        # a = r.listen(source,timeout=2,phrase_time_limit=10)
    try:
        print('Recogniting...') 
        query = r.recognize_google(audio, language= 'en-in')   
        print(f"You said : {query}\n")
    except Exception as e:
        print(e)
        print('Say That again Please')
        return "none"
    return query.lower()       
#Current Time
def timeNow():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(time)
    speak(f"Time now is {time}")
#function to get location
def getLocation():
    
    try:
        ip = requests.get('https://api.ipify.org').text
                    # ip='103.194.91.4'
        print(f"Your IP Address is {ip}")
        url = "http://ip-api.com/json/"+ip
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        city = geo_data['city']
        country = geo_data['country']
        speak(f'Sir, your are in{city} city in {country}')
                 
    except Exception as e :
        speak('Sorry I am  unable to find the location')
        pass 
    return city
#function to know about laptop battery status
def getBatteryDetails():
    battery  = psutil.sensors_battery()
    speak(f"Remaining Battery Precentage {battery.percent}")
    speak(f"Charging Status {str(battery.power_plugged)}")

#to wish 
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak('Good Morning , Sir!')
    elif( hour >=12 and hour<16):
        speak('Good AfterNoon ,Sir!')
    elif( hour >=16 and hour<20 ):
        speak('Good Evening ,Sir!')
    else :
        speak("Good Night Sir!")            
    speak('Hi , I am Jarvis , How can I help you Sir!')
#function to send email
def sendEmail(recipent,message):
    _myEmail = 'your email'
    _myPassword = 'own password'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(_myEmail,_myPassword)
    server.sendmail(_myEmail,recipent,message)
    server.close()
#function to speak newes
def news():
    speak('Do you want me to tell about just top headlines for something else')
    q = takeCommand()
    if 'yes' in q or 'nothing else' in q:
        results = getNews(None)
    else:
        speak('what category of news you want')
        category = takeCommand()
        results = getNews(category)
    for i in range(len(results)):
        speak(f"News {i+1}")
        speak(results[i])
def getWeather(city_name):
    api_key = '4e1e1c04769254970177cb657701f072'
    # city_name = input('Enter the city name')
    apiUrl = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key
    result = requests.get(apiUrl).json()
    # print(result)
    weather = result["weather"]
    # print(weather)
    main = result["main"]
    temp = round(main["temp"] - 273.00 , 2)
    feels_like = round(main["feels_like"]-273,2)
    temp_max = round(main["temp_max"]-273,2)
    temp_min = round(main["temp_min"]-273,2)
    weather_type = weather[0]['main']
    speak(f"{weather_type}y weather")
    speak(f"Current temperature is {temp}°C but feels like {feels_like}°C")

    # speak(f"Maximum temperature of the day would be  {temp_max}°C ")
    # speak(f"Minimum temperature of the day would be  {temp_min}°C")        
if __name__ == "__main__":
    
    # speak("Hellow World this program is written by bibek sen the great")    
    # takeCommand()
    wish()
    # timeNow()
    
    while True:
        query = takeCommand().lower()

        #Tasks Logics

        if 'open ms word' in query:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path)
            speak('opening ms word')
        elif 'open command prompt' in query:
            os.system('start cmd')
        elif 'open camera' in query:
            print('Press Exc button to close the camera')
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()   
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if(k==27):
                    break
            cap.release()
            cv2.destroyAllWindows()    
        elif "play music" in query:
            music_dir = "C:\\Users\\offic\\OneDrive\\Desktop\\My music"
            songs_in_music_dir = os.listdir(music_dir)
            rand_song_select = random.choice(songs_in_music_dir)
            print(rand_song_select)
            os.startfile(os.path.join(music_dir,rand_song_select))
        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")
        elif "wikipedia" in query:
            try:
                speak("Searching wikipedia...")
                query = query.replace("wikipedia","")
                results =  wikipedia.summary(query,sentences = 5)
                speak("According to wikipedia... ")
                speak(results) 
            except Exception as e:
                speak('Sorry sir unable to find on wikipedia')    
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
        elif "search on youtube" in query:
            speak("What do you want to search on youtube")
            search = takeCommand()
            url = "https://www.youtube.com/results?search_query="+search
            webbrowser.open(url)
        elif "search on google" in query:
            speak("What do you want to search on google ?")
            search = takeCommand()
            url = "https://www.google.com/search?q="+search
            webbrowser.open(url)
        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open('https://www.google.com/')
        elif 'open facebook ' in query:
            speak('Checking your messages, Sir') 
            webbrowser.open('https://www.facebook.com/') 
        elif 'open whatsapp' in query:
            speak('opening whatsapp')   
            webbrowser.open('https://web.whatsapp.com/')  
        elif 'open linkedin' in query:
            speak('opening linkdin')
            webbrowser.open('https://www.linkedin.com/feed/')
        elif "send whatsapp message" in query:
            speak('Here is your contact List Sir!')
            printContact()
            speak("Did you found whom you want to message ")
            speak("To add new contact Say")
            speak("Add new contact")
            x = takeCommand()
            if 'add new contact' in x:
                addContact()
            name = selectContact()
            speak("What is the Message!")
            msg = takeCommand()
            sendMessage(name,msg)
        elif "add new contact" in query:
            addContact()    
        elif "play videos on youtube" in query or "play song on youtube" in query:
            speak("Which song do you want  to play ")
            song = takeCommand().lower()
            pywhatkit.playonyt(song)  
        elif "send email" in query:
            try :
                speak("What should I say?")
                message = takeCommand().lower()
                recipent = "sounaksen4@gmail.com"
                sendEmail(recipent,message)
                speak('Mail has been sent to bibek')
            except Exception as e :
                print(e)
                speak('Sorry Sir, Unable to send mail to this email address')       
        elif 'kill yourself' in query:
            speak('Okay Sir, have a good day!')
            sys.exit()  
        elif 'no thanks' in query:
            speak('Okay Sir, Thanks for using me have a good day')
            sys.exit()      
        #to close running applications
        elif "close ms word" in query:
            speak("Closing ms word")
            # os.system('time')
            os.system("taskkill /f /im WINWORD.EXE") #opens cmd and performs the task mentioned
        #to set an alarm
        elif "set alarm" in query:
            hr = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute) 
            if(hr == 23 and min == 16):
                music_dir = "C:\\Users\\offic\\OneDrive\\Desktop\\My music"
                songs_in_music_dir = os.listdir(music_dir)
                rand_song_select = random.choice(songs_in_music_dir)
                print(rand_song_select)
                os.startfile(os.path.join(music_dir,rand_song_select))
        #to close the system
        elif "shutdown the system" in query or 'shut down the system' in query:
            speak('ShutDown Process started')
            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
            speak("Restart Process started")
            os.system('shutdown /r /t 5')    
        #Switch windows
        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt") 
        #Speaks current news sheadlines       
        elif "tell the news" in query or "tell me the news" in query:
            news()
        elif 'what is the time now' in query:
            timeNow()    
        #Find your current locations
        elif "my location" in query:
            speak("Getting your location")
            getLocation()
        elif 'weather report' in query:
            city_name = ''
            speak('Sir, do you want to get weather of your current location')
            ans = takeCommand()
            if 'yes' in ans:
                city_name = getLocation()
                getWeather(city_name)
            else:    
                speak('Enter the name of the city')
                city_name = input('Enter the name of the city :  ')
                getWeather(city_name)
        elif 'bitcoin rates' in query or 'bitcoin rate' in query:
            price = bitcoinPrices()    
            speak(price)
            speak('rupees')
        elif 'vaccine availability' in query :
            speak('Please enter the respective details')
            getVaccine()
            speak("Here are your Results")
        elif 'battery status' in query or 'battery left' in query:
            getBatteryDetails()
        elif 'wish me' in query:
            wish()
        elif "volume up" in query:
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")    
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")        
            pyautogui.press("volumedown")        
            pyautogui.press("volumedown")        
            pyautogui.press("volumedown")
        elif "volume mute" in query or "volume unmute" in query:
            pyautogui.press("volumemute")
        elif "scroll up" in query:
            pyautogui.scroll(150)
        elif "scroll down" in query:
            pyautogui.scroll(-150)    
        elif "page up" in query:
            pyautogui.press('pageup')
        elif "page down" in query:
            pyautogui.press('pagedown')
        elif 'page back' in query:
            pyautogui.press('browserback')       
        elif 'page forward' in query:
            pyautogui.press('browserforward')
        elif 'move to home page' in query or 'home page' in query:
            pyautogui.press('browserhome')
        elif 'refresh the page' in query:
            pyautogui.press('browserrefresh')  
        elif 'launch mail' in query:
            pyautogui.press('launchmail')          
        elif 'well done' in query or "very good" in query or "good work" in query:
            speak('Its my pleasure Sir!')    