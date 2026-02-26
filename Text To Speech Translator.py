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
japanese = Radiobutton(screen, text = 'Japanese', variable = selected_language, value = "ja")
japanese.place(x = 15, y = 375)
french = Radiobutton(screen, text = 'French', variable = selected_language, value = "fr")
french.place(x = 15, y = 435)
sinhalese = Radiobutton(screen, text = 'Sinhalese', variable = selected_language, value = "si")
sinhalese.place(x = 15, y = 495)
german = Radiobutton(screen, text = 'German', variable = selected_language, value = "de")
german.place(x = 15, y = 495)
screen.mainloop()
