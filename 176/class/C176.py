# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:19:16 2022

@author: elect
"""

# Imports
from tkinter import *
from PIL import ImageTk, Image
import speedtest

# Variables

# Function
def checkSpeed():
    speedtestSpeedTest = speedtest.Speedtest()
    labelSpeedDown['text'] = str(round(speedtestSpeedTest.download() / 1000000, 2)) + "mbps"
    labelSpeedUp['test'] = str(round(speedtestSpeedTest.upload() / 1000000, 2)) + "mbps"

# Classes

# --- GUI START ---
window = Tk()

window.title("Speed Test")
window.geometry("500x300")
window.configure(bg="#dee8f1")

# GUI.images

# GUI.ui
# GUI.ui.label
labelHeading = Label(window, text="Internet Speed Test", font=("Lucida Sans Unicode", 20, "bold", "italic"), fg="#5D6D7E", bg="#DEE8F1")

labelSpeedDownHead = Label(window, text="Download Speed", font=("Segow Print", 18, "bold"), fg="#5D6D7E", bg="#DEE8F1")
labelSpeedUpHead = Label(window, text="Internet Speed Test", font=("Segow Print", 18, "bold"), fg="#5D6D7E", bg="#DEE8F1")

labelSpeedDown = Label(window, text="", font=("Yu Gorthic Light", 14, "bold"), fg="#5D6D7E", bg="#DEE8F1")
labelSpeedUp = Label(window, text="", font=("Yu Gorthic Light", 14, "bold"), fg="#5D6D7E", bg="#DEE8F1")

# GUI.ui.button
buttonCheckSpeed = Button(window, text="Check Speed", command=checkSpeed, fg="white", bg="#218796", relief=FLAT)

# GUI.ui.(element.place())
labelHeading.place(relx=0.5, rely=0.1, anchor=CENTER)
labelSpeedDownHead.place(relx=0.25, rely=0.5, anchor=CENTER)
labelSpeedUpHead.place(relx=0.75, rely=0.5)
labelSpeedDown.place(relx=0.25, rely=0.6, anchor=CENTER)
labelSpeedUp.place(relx=0.75, rely=0.6, anchor=CENTER)

buttonCheckSpeed.place(relx=0.5, rely=0.3, anchor=CENTER)

# --- GUI END --

window.mainloop()
