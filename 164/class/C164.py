# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:15:19 2022

@author: elect
"""

# Imports
from tkinter import *
from PIL import ImageTk, Image

# Variables

# Function
def planetInfo():
    print("Hi")

# --- GUI START ---
window = Tk()

window.title("Planet Encyclopedia")
window.geometry("500x500")
window.configure(background="lightblue")

# GUI.images

# GUI.ui
# GUI.ui.label
labelHeading = Label(window, text="Planet: None", bg="lightblue")
labelPlanetName = Label(window, font=("courier", 18, "bold"), bg="lightblue")
labelPlanetImage = Label(window, bg="gold2", highlightthickness=5, borderwidth=2, relief=SOLID)
labelPlanetGravityRadius = Label(window, font=("castellar"), bg="lightblue")
labelPlanetInfo = Label(window, font=("courier", 10, "bold"), bg="lightblue", wraplength=500)

# GUI.ui.button
buttonPlanetInfo = Button(window, text="Show Planet Info", command=planetInfo)

# GUI.ui.(element.place())
labelHeading.place(relx=0.2, rely=0.1, anchor=CENTER)
labelPlanetName.place(relx=0.5, rely=0.25, anchor=CENTER)
labelPlanetImage.place(relx=0.5, rely=0.5, anchor=CENTER)
labelPlanetGravityRadius.place(relx=0.5, rely=0.8, anchor=CENTER)
labelPlanetInfo.place(relx=0.5, rely=0.9, anchor=CENTER)

buttonPlanetInfo.place(relx=0.5, rely=0.18, anchor=CENTER)

# --- GUI END --

window.mainloop()