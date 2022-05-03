import pyttsx3

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice',voices[0].id)
def speak(audio):
engine.say(audio) 
engine.runAndWait()