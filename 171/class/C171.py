# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:15:58 2022

@author: elect
"""

# Imports
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime

import pytz
import time

# Variables

# Function

# Classes
class India:
    def time(self):
        labelTimeIndia['text'] = "Time: " + datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H:%M:%S")
        labelTimeIndia.after(200, self.time)
        
class USA:
    def time(self):
        labelTimeUSA['text'] = "Time: " + datetime.now(pytz.timezone('US/Central')).strftime("%H:%M:%S")
        labelTimeUSA.after(200, self.time)

# --- GUI START ---
window = Tk()

window.title("PyTITUSA - Python Time India to Time USA")
window.geometry("600x600")
window.configure(background="white")

# GUI.class
indiaIndiaTime = India()
usaUSATime = USA()

# GUI.images
imageClock = ImageTk.PhotoImage(Image.open("assets/clock.jpg"))

# GUI.ui
# GUI.ui.label
labelClockImageIndia = Label(window, image=imageClock)
labelClockImageUSA = Label(window, image=imageClock)

labelCountryIndia = Label(window, text="India")
labelTimeIndia = Label(window)

labelCountryUSA = Label(window, text="USA")
labelTimeUSA = Label(window)

# GUI.ui.button
buttonIndiaShowTime = Button(window, text="Show Time", command=indiaIndiaTime.time)
buttonUSAShowTime = Button(window, text="Show Time", command=usaUSATime.time)

# GUI.ui.(element.place())
labelClockImageIndia.place(relx=0.2, rely=0.35, anchor=CENTER)
labelClockImageUSA.place(relx=0.7, rely=0.35, anchor=CENTER)

labelCountryIndia.place(relx=0.2, rely=0.05, anchor=CENTER)
labelTimeIndia.place(relx=0.2, rely=0.65, anchor=CENTER)

labelCountryUSA.place(relx=0.7, rely=0.05, anchor=CENTER)
labelTimeUSA.place(relx=0.7, rely=0.65, anchor=CENTER)

buttonIndiaShowTime.place(relx=0.2, rely=0.8, anchor=CENTER)
buttonUSAShowTime.place(relx=0.7, rely=0.8, anchor=CENTER)

# --- GUI END --

window.mainloop()