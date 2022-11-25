# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 18:13:21 2022

@author: elect
"""

# Imports
from tkinter import Tk, Label, Button, StringVar, SOLID, CENTER, messagebox
from tkinter import ttk
from PIL import ImageTk, Image

# Variables
listPlanets = ["Mercury", "Venus", "Earth"]
dictatoryPlanetsInfo = {"Mercury": {"Gravity": "3.7m/s²", "Radius": "2,438.7km", "Info": ""}, "Venus": {"Gravity": "8.97m/s²", "Radius": "", "Info": ""}, "Earth": {"Gravity": "9.807m/s²", "Radius": "", "Info": ""}}

# Function
def planetInfo():
    local_strPlanetName = strvarSelPlanetName.get()
    try:
        labelPlanetImage['image'] = dictatoryImages[local_strPlanetName]
        labelPlanetName['text'] = local_strPlanetName
        labelPlanetGravityAndRadius['text'] = "Gravity:" + dictatoryPlanetsInfo[local_strPlanetName]["Gravity"] + "\nRadius: " + dictatoryPlanetsInfo[local_strPlanetName]["Radius"]
        labelPlanetInfo['text'] = dictatoryPlanetsInfo[local_strPlanetName]["Info"]
    except KeyError:
        messagebox.showerror("Planet Not Found", "Planet \"" + local_strPlanetName + "\" is not found in our database!")

# --- GUI START ---
window = Tk()

window.title("Planet Encyclopedia")
window.geometry("500x500")
window.configure(background="lightblue")

# GUI.variables
strvarSelPlanetName = StringVar()

# GUI.images
imageMercury = ImageTk.PhotoImage(Image.open("assets/mercury.jpg"))
imageVenus   = ImageTk.PhotoImage(Image.open("assets/venus.jpg"))
imageEarth   = ImageTk.PhotoImage(Image.open("assets/earth.jpg"))
dictatoryImages = {"Mercury": imageMercury, "Venus": imageVenus, "Earth": imageEarth}

# GUI.ui
# GUI.ui.label
labelHeading = Label(window, text="Select Planet: ", bg="lightblue")
labelPlanetName = Label(window, font=("courier", 18, "bold"), bg="lightblue")
labelPlanetImage = Label(window, bg="gold2", highlightthickness=5, borderwidth=2, relief=SOLID)
labelPlanetGravityAndRadius = Label(window, font=("castellar"), bg="lightblue")
labelPlanetInfo = Label(window, font=("courier", 10, "bold"), bg="lightblue", wraplength=500)

# GUI.ui.button
buttonPlanetInfo = Button(window, text="Show Planet Info", command=planetInfo)

# GUI.ui.other
dropdownPlanetName = ttk.Combobox(window, values=listPlanets, textvariable=strvarSelPlanetName)

# GUI.ui.(element.place())
labelHeading.place(relx=0.2, rely=0.1, anchor=CENTER)
labelPlanetName.place(relx=0.5, rely=0.25, anchor=CENTER)
labelPlanetImage.place(relx=0.5, rely=0.5, anchor=CENTER)
labelPlanetGravityAndRadius.place(relx=0.5, rely=0.8, anchor=CENTER)
labelPlanetInfo.place(relx=0.5, rely=0.9, anchor=CENTER)

buttonPlanetInfo.place(relx=0.5, rely=0.18, anchor=CENTER)

dropdownPlanetName.place(relx=0.5, rely=0.1, anchor=CENTER)

# --- GUI END --

window.mainloop()