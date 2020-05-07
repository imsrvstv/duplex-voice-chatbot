import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as ScrolledText

root = tk.Tk()
root.title('DUPLEX')
root.resizable(0, 0)
root.config(width=400, height=600,bg='white')


label0=tk.Label(master=root,text='DUPLEX : A VOICE ASSISTANT', bg='#e74c3c',font=("Courier", 15),width=56,height=2,fg='white')
label0.pack()
label0.place(relx=0.5,rely=0.04, anchor=CENTER)


convo = ScrolledText.ScrolledText(width=49, height=31,fg='blue')
convo.place(relx=0.0,rely=0.07)


def center_window(w=400, h=600):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
center_window()

from starterkit.fallback_module.get_smart_answer import get_smart_answer
from mgr.mgr_db import db_loadEnabledModules


import speech_recognition as sr
r = sr.Recognizer()
import pyttsx3

ENABLED_MODULES = db_loadEnabledModules()
FALLBACK_MODULE = get_smart_answer() 

assistantVoice = pyttsx3.init()

def configureAssistantVoice():
    
    assistantVoice.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

    
    assistantVoice.setProperty('rate',150)

def getAssistantResponse(phrase):
    have_answered = False
    answer = "Unknown error"
    global convo
    for module in ENABLED_MODULES:
        
        if any(x in str(phrase) for x in module.getChatKeywords()):
            answer = str(module.getAnswer(phrase))
            have_answered = True

    
    if not have_answered: answer = str(FALLBACK_MODULE.getAnswer(phrase))

    print("Assistant response: \""+answer+"\"")
    convo.insert("end","\n\n"+answer, ("centered",))
    convo.tag_configure("centered", justify="left")
    convo.config(fg='red')

    assistantVoice.say(answer)
    assistantVoice.runAndWait()


def live_speech():
    print("Starting speech recognition.")
    c=0
    global convo
    with sr.Microphone() as source:
        while True:
            if(c==1):
                break;
            try:
                audio = r.listen(source,phrase_time_limit=10)
                
                text = r.recognize_google(audio, language="en-US")
                print("Users message: '{}'".format(text))
                if(text.strip()=='bye'):
                    c=1
                convo.insert("end","\n\n"+text, ("centered",))
                convo.tag_configure("centered", justify="right")
                convo.config(fg='blue')
                getAssistantResponse(text)
            except sr.UnknownValueError:
                print("Sorry, I could not understand you.")
            except sr.RequestError:
                print("API call failed. Key valid? Internet connection?")

try:
    configureAssistantVoice()
except:
    print("VoiceMgr: Could not configure assistants speech. Using default settings.")

root.after(2000,live_speech)
root.mainloop()
