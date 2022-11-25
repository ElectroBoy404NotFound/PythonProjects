# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 18:05:32 2022

@author: elect
"""

# Imports
from tkinter import *
from PIL import ImageTk, Image

# Variables
intOldX = 50
intOldY = 50
intNewX = 50
intNewY = 50

# Function
def directionLeft(e):
    global intOldX
    global intOldy
    global intNewX
    global intNewY
    
    intOldX = intNewX
    intOldY = intNewY
    intNewX = intNewX - 5
    
    draw(intOldX, intOldY, intNewX, intNewY)

def directionRight(e):
    global intOldX
    global intOldy
    global intNewX
    global intNewY
    
    intOldX = intNewX
    intOldY = intNewY
    intNewX = intNewX + 5
    
    draw(intOldX, intOldY, intNewX, intNewY)
    
def directionUp(e):
    global intOldX
    global intOldy
    global intNewX
    global intNewY
    
    intOldX = intNewX
    intOldY = intNewY
    intNewY = intNewY - 5
    
    draw(intOldX, intOldY, intNewX, intNewY)
    
def directionDown(e):
    global intOldX
    global intOldy
    global intNewX
    global intNewY
    
    intOldX = intNewX
    intOldY = intNewY
    intNewY = intNewY + 5
    
    draw(intOldX, intOldY, intNewX, intNewY)
    
def draw(intOldX, intOldY, intNewX, intNewY):
    local_strFillColor = entryColor.get()
    canvas.create_line(intOldX, intOldY, intNewX, intNewY, width=3, fill=local_strFillColor)

# --- GUI START ---
window = Tk()

window.title("")
window.geometry("600x600")

# GUI.images

# GUI.ui
# GUI.ui.label
labelColor = Label(window, text="Enter a Color")

# GUI.ui.button

# GUI.ui.entry
entryColor = Entry(window)
entryColor.insert(0, "black")

# GUI.ui.canvas
canvas = Canvas(window, width=590, height=510, bg="white", highlightbackground="lightgray")
canvasImageArtist = canvas.create_image(50, 50, image=ImageTk.PhotoImage(Image.open("assets/start_point1.png")))

# GUI.ui.(element.place())
labelColor.place(relx=0.6, rely=0.9, anchor=CENTER)
entryColor.place(relx=0.8, rely=0.9, anchor=CENTER)
canvas.pack()

# GUI.ui.keyevents
window.bind("<Right>", directionRight)
window.bind("<Left>", directionLeft)
window.bind("<Up>", directionUp)
window.bind("<Down>", directionDown)

# --- GUI END --

window.mainloop()
