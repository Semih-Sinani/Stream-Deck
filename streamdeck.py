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
        search_text_entry.delete("1.0", tk.END
                                 
                                 def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="tr-TR")
        search_text_entry.delete("1.0", tk.END)
        search_text_entry.insert(tk.END, text)
    except sr.UnknownValueError:
        search_text_entry.delete("1.0", tk.END)
        search_text_entry.insert(tk.END, "Ses anlaşılamadı.")
    except sr.RequestError as e:
        search_text_entry.delete("1.0", tk.END)
        search_text_entry.insert(tk.END, "Ses tanıma servisine erişilemedi; {0}".format(e))

def perform_search():
    query = search_text_entry.get("1.0", tk.END).strip()
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
    else:
        search_text_entry.delete("1.0", tk.END)
        search_text_entry.insert(tk.END, "Arama yapılacak kelime veya cümleyi girin.")

def show_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    search_text_entry.delete("1.0", tk.END)
    search_text_entry.insert(tk.END, f"Şu an saat: {current_time}")



def return_to_main_screen():
    if commands_window:
        commands_window.destroy()
        
 
def open_commands():
    global commands_window
    commands_window = tk.Toplevel(window)
    commands_window.title("Komutlar") #komutlar sekmesi

    command_list = [
        {
            "name": "Arama Yap",
            "action": perform_search
        },
        {
            "name": "Yazıyı Sese Çevir (Türkçe)",
            "action": lambda: text_to_speech("tr")
        },
        {
            "name": "Yazıyı Sese Çevir (İngilizce)",
            "action": lambda: text_to_speech("en")
        },
        {
            "name": "Sesi Yazıya Çevir",
            "action": speech_to_text
        },
        {
            "name": "Saat Göster",
            "action": show_time
        }
        # Diğer komutları buraya ekleyebilirsiniz
    ]