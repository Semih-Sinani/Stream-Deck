import tkinter as tk #arayüz oluşturucu
import speech_recognition as sr #sesli kontrıl kütüphanesii
import pyttsx3
import webbrowser #chrome bağlan
import datetime

def recognize_speech_for_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)