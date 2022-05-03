import nltk  
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import numpy as np
import string
import random 
import pyttsx3
import random
import speech_recognition as sr
import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from lxml import html
from bs4 import BeautifulSoup
from googlesearch import search
#tokenization
#text="NLP abs bcd"
#print(sent_tokenize(text))
# print(word_tokenize(text))
#lemmatization
#lemat= WordNetLemmatizer()
#print("better",lemat.lemmatize("better",pos="a"))
#stemming
#ps = PorterStemmer()
#w=["likes","liked","liking"]
#for e in w:
#    print(e,":",ps.stem(e)) 
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.setProperty("rate",160)
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
lemmer=nltk.stem.WordNetLemmatizer
def LemTokens(tokens):
    return[lemmer.lemmatize(token) for token in tokens]
remove_punct=dict((ord(punct),None) for punct in string.punctuation)
def LemNormal(text):
    return LemTokens(nltk.word_tokenize(text.translate(remove_punct)))
def response(statement):
    robo1_response=''
    tfidvec=TfidfVectorizer(tokenizer=LemNormal,stop_words='english')
    #tfidf=tfidvec.fit_transform(sent_tokens)
greet=("hello","hi","greetings","sup","what's up","whats up","hey",)
responses=["hi","hey ","nods","hi there","hello","I am glad! You are talking to me"]
def greeting(statement):
    for word in statement.split():
        if word in greet:
            return random.choice(responses)  

if __name__=='__main__':
    print("Loading your AI personal assistant AREUM")
    speak("Loading your AI personal assistant AREUM")
    gretings() 
    statement =takeCommand()
    speak(greeting(statement))
   # while True:
    #    speak("Tell me how can I help you ?")
     #   statement =takeCommand()
      #  if statement==0:
       #     continue
        #if "good bye" in statement or "ok bye" in statement or "stop" in statement:
         #   speak('your personal assistant is shutting down,Good bye')
          #  print('your personal assistant is shutting down,Good bye')
           # break
