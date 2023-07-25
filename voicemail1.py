from email import message

import pyttsx3

import speech_recognition as sr

import smtplib

import os

import datetime


engine=pyttsx3.init()

voices=engine.getProperty('voices')

engine.setProperty('voices',voices[1].id)

engine.setProperty('rate',180)

def speak(sentence):

   engine.say(sentence)

   print("Machine said::"+sentence)

   engine.runAndWait()


def takeCommand():

    r=sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening......")

        r.pause_threshold=1

        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)

    try:

        print("Recognizing...")

        query=r.recognize_google(audio,language='en-in')

        print(f"User said:{query}\n")

    except Exception as e:

        speak("No message")

        return "None" 


   
    query=query.lower()

    return query

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


def mail():
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    speak("Wait a second logging in...")
    sender_mail_id=os.environ.get('EMAIL_ID')
    password=os.environ.get('EMAIL_PASSWORD')
    s.login(sender_mail_id,password)
    speak("Logged in")
    speak("Please enter the receiver's mail id")
    receiver_mail_id=input("Enter here::")
    speak("What is the message?")
    message=takeCommand()
    s.sendmail(sender_mail_id,receiver_mail_id,message)
    speak("Sending Mail...")
    s.quit()
    speak("Mail sent successfully")



if __name__=='__main__':
    wishme()
    mail()    


  