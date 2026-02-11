#It is a Python-Based personal A.I Assistant named E.L.I.N.A designed to increase workflow and help reduce work
#It plays a random Music and movie wishes good morning.good afternoon,good evening and good night based of system time and also tells weather report of the given location
#if available it also opens games and tells the lastest 5 news
#The modules used are pyttsx3,datetime,wikipedia,webbrowser,os,random,requests
#since I do not have a Microphone I did not use speechrecognition
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import requests

def speak(audio):
    """
    main speak function where voice , rate and volume is controlled and for every speak engine is initialized

    """
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")

    engine.setProperty("voice", voices[1].id)#uses the default microsoft voice ZIRA
    engine.setProperty("rate", 130)#controls the speed of the speech
    engine.setProperty("volume", 0.8)#controls the volume of the speech
    engine.say(audio)#says the string written
    engine.runAndWait()#This ensures that the text is spoken and wait until its over.Without this speak wont work

def say_time():
    """
    Tells the current Time
    """
    n=datetime.datetime.now().strftime("%Y-%m-%d %H:%M %p")#time is formatted to year,month,date and hour:Minute (standard Meridian)
    b=datetime.datetime.now().strftime("%H:%M %p")#time is formatted to
    if(n>="5:00 AM" and n<="12:00 PM"):
        speak("Good Morning Sir Time, is " + b)
    elif(n>"12:00 PM" and n<="5:00 PM"):
        speak("Good Afternoon Sir, Time is" + b)
    elif(n>"5:00 PM" and n<="7:00 PM"):
        speak("Good Evening Sir, Time is" + b)
    elif(n>="9:00 PM"):
        speak("Good Night Sir")

def say_date():
    """
    Tells the current date
    """
    d = datetime.datetime.now().strftime("%Y-%m-%d")#time is formatted to date format
    speak("Todays Date is")
    speak(d)

def music():
    """ plays a Random Music """
    music_location="C:\\Users\\Admin\\Music\\Music"
    l1=os.listdir(music_location)#gives the contents of the folder in list
    b=len(l1)
    a=random.randint(0,b)
    os.startfile(os.path.join(music_location,l1[a]))#it helps in starting the file and join function joins the location with the music choosen by random
    return l1[a]#returns the choosen song_name


def open_cuphead():#(optional)
    """
    opens Cuphead Game(if available in the directory)
    """
    exe_loc="E:\\Games\\Cuphead"
    l2=os.listdir(exe_loc)
    os.startfile(os.path.join(exe_loc,l2[3]))#opens the exe file
def open_ER():#optional
    """
    opens Elden Ring Game(if available in the directory)

    """
    loc="E:\\Games\\ELDEN RING\\Game"
    l3=os.listdir(loc)
    os.startfile(os.path.join(loc,l3[14]))#opens the exe file
def open_movies():
    """
    plays a Random Movie
    """
    loc="C:\\Users\\Admin\\Desktop\\Movies"
    l4=os.listdir(loc)
    a=len(l4)
    b=random.randint(0,a)
    os.startfile(os.path.join(loc,l4[b]))#it helps in starting the file and join function joins the location with the movie choosen by random
    return l4[b]#returns the choosen movie_name

def open_VS():
    """
    opens VS Code(if present)
    """
    loc="C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code"
    l5=os.listdir(loc)
    os.startfile(os.path.join(loc,l5[4]))#opens VS Code

def news():
    """
    Fetch The Latest News Using newsdata.io api
    """
    r = requests.get("https://newsdata.io/api/1/latest?apikey="write API_KEY")
    url = "https://newsdata.io/api/1/latest"
    params = {
        "apikey": "write API_KEY",
        "language": "en",
    }
    response = requests.get(url, params=params)  # Retrieve the news
    data = response.json()  # converts the retrieved news in JSON format to python structure
    title = data["results"]  # contain list of dictionaries
    news_order = [
        "First", "Second", "Third", "Fourth", "Fifth",
        "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"
    ]
    for j, i in enumerate(title[:5]):
        t = i.get("title", "no title available")
        descrip = i.get("description", "No available news")
        speak(f"{news_order[j]} News Title")
        speak(t)
        speak(f"{news_order[j]} News Description")
        speak(descrip)

def W_report():
    """
    Tells the weather report the location given
    """
    g=str(input("Enter Location:-"))#takes the location
    URL="http://api.openweathermap.org/geo/1.0/direct?"#Base URL
    params={
        "q":f"{g}",
        "appid":"Write API KEY"#API_KEY
    }
    r=requests.get(URL,params=params)
    data = r.json()#returns the list of dictionaries with the location's latitude and longitude
    l1 = data[0]["lat"]#access the latitude
    l2 = data[0]["lon"]#access the longitude
    URL="https://api.openweathermap.org/data/2.5/weather"#Base URL
    params={
        "lat":f"{l1}",#takes the latitude fetched from data
        "lon":f"{l2}",#takes the longitude fetched from data
        "units":"metric",#returns the weather report in metric units
        "appid":"Write API KEY"#API_KEY
    }
    r=requests.get(URL,params=params)
    data1 = r.json()#returns the list of dictionaries
    speak(f"Location is {g}")
    print(f"Location is {g}")
    h=data1["weather"]#fetch the value of the key "weather"
    n=h[0]["description"]#The Value fetched is in list of dictionaries so we took the description part
    speak(f"The Weather is {n}")
    print(f"The Weather is {n}")
    speak(f"The Temperature is {int(data1["main"]["temp"])} degree celcius")#tells the temperature
    print(f"The Temperature is {int(data1["main"]["temp"])}%C")#tells the temperature
    speak(f"The Humidity is {data1["main"]["humidity"]}%")#tells the humidity
    print(f"The Humidity is {data1["main"]["humidity"]}%")#tells the humidity
    speak(f"The Wind Speed is {data1["wind"]["speed"]}kilometer per hour")#tells the wind speed
    print(f"The Wind Speed is {data1["wind"]["speed"]} km/hr")#tells the wind speed


if __name__ == '__main__':
    speak("I am Elina Your Own Personal AI assistant How may I help you")
    speak("Please Enter Your Commands")
    while True:
        try:
            command=str(input("Enter Command:")).lower()
            if "time" in command:#checks the keyword "time" in command to initiate the say_time() function
                say_time()
            elif "date" in command:
                say_date()
            elif "weather" in command:
                speak("Please Enter the Location")
                W_report()
            elif "youtube" in command or "yt" in command:#if the keyword "youtube" or "yt" is present then webbrowser opens the website
                speak("Opening Youtube")
                webbrowser.open("https://www.youtube.com/")
            elif "google" in command:
                speak("opening Google")
                webbrowser.open("https://www.google.com/")
            elif "leetcode" in command:
                speak("opening Leetcode")
                webbrowser.open("https://leetcode.com/")
            elif "gmail" in command or "mail" in command or "email" in command:
                speak("opening Mail")
                webbrowser.open("https://mail.google.com/")
            elif "github" in command:
                speak("opening GitHub")
                webbrowser.open("https://github.com/")
            elif "discord" in command:
                speak("opening Discord")
                webbrowser.open("https://discord.com/")
            elif "chatgpt" in command:
                speak("opening ChatGPT")
                webbrowser.open("https://chatgpt.com/")
            elif "stackoverflow" in command:
                speak("opening StackOverflow")
                webbrowser.open("https://stackoverflow.com/")
            elif "reddit" in command:
                speak("opening Reddit")
                webbrowser.open("https://www.reddit.com/")
            elif "quora" in command:
                speak("opening Quora")
                webbrowser.open("https://www.quora.com/")
            elif "twitter" in command:
                speak("opening twitter")
                webbrowser.open("https://www.twitter.com/")
            elif "instagram" in command:
                speak("opening enstagram")
                webbrowser.open("https://www.instagram.com/")
            elif "facebook" in command:
                speak("opening Facebook")
                webbrowser.open("https://www.facebook.com/")
            elif "deepseek" in command:
                speak("opening DeepSeek")
                webbrowser.open("https://www.deepseek.com/en")
            elif "whatsapp" in command:
                speak("opening WhatsApp")
                webbrowser.open("https://www.whatsapp.com/")
            elif "telegram" in command:
                speak("opening Telegram")
                webbrowser.open("https://web.telegram.org/")
            elif "pinterest" in command:
                speak("opening Pinterest")
                webbrowser.open("https://www.pinterest.com/")
            elif "flipkart" in command:
                speak("opening Flipkart")
                webbrowser.open("https://www.flipkart.com/")
            elif "amazon" in command:
                speak("opening Amazon")
                webbrowser.open("https://www.amazon.com/")
            elif "meesho" in command:
                speak("opening Meesho")
                webbrowser.open("https://www.meesho.com/")
            elif "myntra" in command:
                speak("opening Myntra")
                webbrowser.open("https://www.myntra.com/")
            elif "netflix" in command:
                speak("opening Netflix")
                webbrowser.open("https://www.netflix.com/")
            elif "prime video" in command:
                speak("opening Amazon Prime Video")
                webbrowser.open("https://www.primevideo.com/")
            elif "hotstar" in command:
                speak("opening Jio Hotstar")
                webbrowser.open("https://www.hotstar.com/")
            elif "disney+" in command:
                speak("opening Disney Plus")
                webbrowser.open("https://www.disneyplus.com/")
            elif "canva" in command:
                speak("opening Canva")
                webbrowser.open("https://www.canva.in/")
            elif "linkedin" in command:
                speak("opening LinkedIn")
                webbrowser.open("https://www.linkedin.com/")
            elif "wikipedia" in command:
                try:
                    command=command.replace("wikipedia","")#see's the keyword "wikipedia" and then replace it to empty string i.e remove wikipedia
                    results=wikipedia.summary(command,sentences=3)#after replacing it matches the previous lines through wikipedia API to get a match if there is a match it returns a summary limited to 3 sentences
                    speak("According to Wikipedia")
                    speak(results)
                except wikipedia.DisambiguationError as e:#Wikipedia error for specific search as the search contain multiple details
                    speak("Please Be More Specific")
                    print("Provide Specific Details")
                except wikipedia.PageError as f:#wikipedia error for page as it couldnt find the wikipedia page for the search
                    speak("I Could not Find anything Related to the Search")
                    speak("Please provide relevant Search")
                    print("Provide Relevant Search")
            elif "cuphead" in command:
                speak("Opening Cuphead")
                open_cuphead()
            elif "elden ring" in command:
                speak("Opening Elden Ring")
                open_ER()
            elif "music" in command or "song" in command:
                music_is = music()
                speak(f"Playing Music{music_is}")#says the music which is being played(takes the return value of function)
            elif "movie" in command or "film" in command or "cinema" in command:
                movie_is = open_movies()
                speak(f"Starting Movie{movie_is}")#says the movie name which is being played(takes the return value of function)
            elif "vs code" in command:
                speak("Opening VS Code")
                open_VS()
            elif "news" in command:
                speak("Fetching Latest News")
                news()
            else:
                speak("Please Enter Valid Commands")
                print("Please Enter valid Commands")
        except Exception as e:

            print("Enter Valid Keywords for Elina to Understand")