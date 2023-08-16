import tkinter as tk #arayüz oluşturucu
import speech_recognition as sr #sesli kontrıl kütüphanesii
import pyttsx3
import webbrowser #chrome bağlan
import datetime

def recognize_speech_for_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

          try:
        text = r.recognize_google(audio, language="tr-TR")
        search_text_entry.delete("1.0", tk.END)
        search_text_entry.insert(tk.END, text)
        perform_search()
    except sr.UnknownValueError:
        search_text_entry.delete("1.0", tk.END)
        search_text_entry.insert(tk.END, "Ses anlaşılamadı.")
    except sr.RequestError as e:
        search_text_entry.delete("1.0", tk.END)
        search_text_entry.insert(tk.END, "Ses tanıma servisine erişilemedi; {0}".format(e))
#hatalara sonuç ata
def text_to_speech(lang):
    text = search_text_entry.get("1.0", tk.END).strip()
    if text:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)  # Ses hızını ayarlayabilirsin
        engine.setProperty("volume", 0.8)  # Ses düzeyini ayarlayabilirsin
        engine.setProperty("voice", lang)  # Seçilen dili ayarlar
        engine.say(text)
        engine.runAndWait()
        search_text_entry.delete("1.0", tk.END)
    else:
        search_text_entry.delete("1.0", tk.END)