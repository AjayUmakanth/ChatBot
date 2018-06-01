from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import os
import pyttsx3;
import wikipedia
import wolframalpha
import win32com.client as wincl
r=sr.Recognizer()
app_id="place your wolframalpha id here"
client = wolframalpha.Client(app_id)
bot=ChatBot('MyChat')
bot.set_trainer(ListTrainer)
##########################################
#
# Uncomment the below lines while running the program for first time to train your bot.
# Then comment it back ll the other times you run this code
# This is because you dont want to again train your already trained bot (and wait each time for i to get trained)
#
############################################
#bot.train("chatterbot.corpus.english")
#To train:
#link='C:\\Users\\ajay umakanth\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english'
#for files in os.listdir(link):
#   data=open(link+"\\"+files,'r').readlines()
#   bot.train(data)
 
def speak(audioString):
    speak=wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(audioString)
def search(querry):
    try:
        res=client.query(querry)
        answer=next(res.results).text
        answer = string.replace (answer, "Wolfram|Alpha", "J.A.R.V.I.S")
        print("Comp: "+answer)
    except:
        try:
            answer=wikipedia.summary(querry,sentences=2)
            print("Comp: "+answer)
        except:
            print("Sorry im incapble of that")

def getVoiceInput():
    print("speak now")
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        message=r.recognize_google(audio)
        print("You: "+str(message))
    except sr.UnknownValueError:
        message="Sorry, I could not understand you"
    except sr.RequestError as e:
        message="Sorry, could not request results from Google Speech Recognition service; {0}".format(e)
    finally:
        return speech.input()
def chatbot(message):
    return bot.get_response(message)
while True:
# For voice input, uncomment below line
#    message=getVoiceInput()

# For keyboard input, uncomment below line
    message=input("You: ")
    reply=chatbot(message)
    
    print("MyComp: "+str(reply))
    speak(reply)
