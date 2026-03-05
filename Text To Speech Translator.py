from tkinter import *
from gtts import gTTS
#Stands for Google Text To Speech
from translate import Translator 
import os

screen = Tk()
screen.geometry("700x700")
screen.title("Text To Speech Translator")
screen.config(background = 'dark olive green')
title1 = Label(screen, text = "Text To Speech Translator", bg = "olive drab", fg = "khaki", font = ("times", 40, "bold"))
title1.place(x = 45, y = 100)
title3 = Entry(screen, bd = 5, bg = "dim gray", fg = "snow3", width = 60, font = ("times", 15, "bold"))
title3.place(x = 45, y = 250)
languages = {"Japanese" : 'ja', "French" : 'fr', "Sinhalese" : 'si', "German" : 'de'}
selected_language = StringVar(value="ja")
japanese = Radiobutton(screen, text = 'Japanese', variable = selected_language, value = "ja", font = ("times", 15, "bold"))
japanese.place(x = 15, y = 375)
french = Radiobutton(screen, text = 'French', variable = selected_language, value = "fr", font = ("times", 15, "bold"))
french.place(x = 15, y = 435)
sinhalese = Radiobutton(screen, text = 'Sinhalese', variable = selected_language, value = "si", font = ("times", 15, "bold"))
sinhalese.place(x = 15, y = 495)
german = Radiobutton(screen, text = 'German', variable = selected_language, value = "de", font = ("times", 15, "bold"))
german.place(x = 15, y = 555)
def trans():
    translator = Translator(to_lang = selected_language.get())
    ttt = title3.get()
    translated_text = translator.translate(ttt)
    myobj = gTTS(text = translated_text, lang = selected_language.get())
    myobj.save("convert.mp3")
submit = Button (screen, text = "Submit", bg = "olive drab", fg = "khaki", width = 40, font = ("times", 20, "bold"), command = trans)
submit.place(x = 25, y = 625)
screen.mainloop()
