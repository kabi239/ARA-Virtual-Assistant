
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import time
import webbrowser
import winsound
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
import pywhatkit as kt
from playsound import playsound
from googletrans import Translator
from gtts import gTTS
import os

flag = 0
dic = ('afrikaans', 'af', 'albanian', 'sq', 
       'amharic', 'am', 'arabic', 'ar',
       'armenian', 'hy', 'azerbaijani', 'az', 
       'basque', 'eu', 'belarusian', 'be',
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
       'bg', 'catalan', 'ca', 'cebuano',
       'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)',
       'zh-tw', 'corsican', 'co', 'croatian', 'hr',
       'czech', 'cs', 'danish', 'da', 'dutch',
       'nl', 'english', 'en', 'esperanto', 'eo', 
       'estonian', 'et', 'filipino', 'tl', 'finnish',
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
       'gl', 'georgian', 'ka', 'german',
       'de', 'greek', 'el', 'gujarati', 'gu',
       'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
       'hi', 'hmong', 'hmn', 'hungarian',
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian', 
       'id', 'irish', 'ga', 'italian',
       'it', 'japanese', 'ja', 'javanese', 'jw',
       'kannada', 'kn', 'kazakh', 'kk', 'khmer',
       'km', 'korean', 'ko', 'kurdish (kurmanji)', 
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian',
       'lt', 'luxembourgish', 'lb',
       'macedonian', 'mk', 'malagasy', 'mg', 'malay',
       'ms', 'malayalam', 'ml', 'maltese',
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
       'mn', 'myanmar (burmese)', 'my',
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
       'pashto', 'ps', 'persian', 'fa',
       'polish', 'pl', 'portuguese', 'pt', 'punjabi', 
       'pa', 'romanian', 'ro', 'russian',
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
       'serbian', 'sr', 'sesotho', 'st',
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'somali', 'so', 'spanish', 'es', 'sundanese',
       'su', 'swahili', 'sw', 'swedish',
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
       'te', 'thai', 'th', 'turkish',
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
       'ug', 'uzbek',  'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu')

engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.setProperty("rate",165)
    engine.say(text)
    engine.runAndWait()

def gretings():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("hello, Good Morning")
        print("hello, Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
           statement=r.recognize_google(audio,language='en-in')
           print(f"user said:{statement}\n")

        except Exception as e:
            speak("Can you please repeat")
            return "None"
         
    return statement.lower()
def tellDay():
    
    day = datetime.datetime.today().weekday() + 1
      
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
def tellTime():
      
    # This method will give the time
    time = str(datetime.datetime.now())
      
    # the time will be displayed like 
    # this "2020-06-05 17:50:14.582630"
    #nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is " + hour + "Hours and" + min + "Minutes")   

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('1803010117@gmail.com', 'khushboosharma239')
    server.sendmail('1803010117@gmail.com', to, content)
    server.close()

def timer (remider,seconds):
    notificator=ToastNotifier()
    notificator.show_toast("Reminder",f"""Alarm will go off in {seconds} Seconds.""",duration=20)
    notificator.show_toast(f"Reminder",remider,duration=20)

    #alarm
    frequency=2500
    duration=1000
    winsound.Beep(frequency,duration)
def destination_language():
    # Input destination language in
    # which the user wants to translate
    to_lang = takeCommand()
    while (to_lang == "None"):
        to_lang = takeCommand()
    to_lang = to_lang.lower()
    return to_lang
  

    
if __name__=='__main__':
    print("Loading your AI personal assistant ARA")
    speak("Loading your AI personal assistant ARA")
    gretings() 

    while True:
        speak("Tell me how can I help you ?")
        statement =takeCommand()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant is shutting down,Good bye')
            print('your personal assistant is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(5)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        
        elif 'open news' in statement:
            news = webbrowser.open_new_tab(' https://timesofindia.indiatimes.com/home/headlines%E2%80%9D' )
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'write an email' in statement:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("To whome should i send?")
                to = takeCommand()    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! your email was not sent")

        elif 'the time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" the time is {strTime}")  

        elif "day it is" in statement:
            tellDay()
            continue
          
        elif "tell me the time" in statement:
            tellTime()
            continue  
        elif "set an alarm" in statement:
            speak("What is the alarm in relation to?: ")
            words=takeCommand()
            time.sleep(2)
            speak("For how many seconds: ")
            sec= takeCommand()
            time.sleep(1)
            timer(words,int(sec) )
        elif "search for me" in statement:
            speak("what do you want me to search")
            target=takeCommand()
            time.sleep(1)
            kt.search(target)
        elif "repeat after me" in statement:
            speak("what would you like me to repeat?")
            input1=takeCommand()
            time.sleep(3)
            speak("you said"+" "+input1)
            print()
        elif "what can you do" in statement:
            speak("I am glad you asked i can do many things ...  like I can tell you time, do search for you , open youTube ,set an alarm and many more")
            print("I am glad you asked i can do many things ...  like I can tell you time, do search for you , open youTube ,set an alarm and many more")
        elif "can you translate" in statement:
            speak("what language should i translate to")
            to_lang = destination_language()
            while (to_lang not in dic):
                print("Language in which you are trying\
                to convert is currently not available ,\
                please input some other language")
            #to_lang = destination_language()
  
            to_lang = dic[dic.index(to_lang)+1]
# invoking Translator
            translator = Translator()
            speak("What would you like to translate")
            query=takeCommand()
  # Translating from src to dest
            text_to_translate = translator.translate(query, dest=to_lang)
            text = text_to_translate.text
# Using Google-Text-to-Speech ie, gTTS() method
# to speak the translated text into the
# destination language which is stored in to_lang.
# Also, we have given 3rd argument as False because
# by default it speaks very slowly
            speak = gTTS(text=text, lang=to_lang, slow=False)
# Using save() method to save the translated
# speech in capture_voice.mp3
            speak.save("captured_voice.mp3")
# Using OS module to run the translated voice.
            playsound('captured_voice.mp3')
            os.remove('captured_voice.mp3')
# Printing Output
            print(text)
            


       