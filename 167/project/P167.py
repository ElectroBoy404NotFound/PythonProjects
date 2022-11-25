# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:29:11 2022

@author: elect
"""

# Imports
from tkinter import *
from PIL import ImageTk, Image

# Variables

# Functions
def rectangle(e):
    canvas.create_line(int(entryStartX.get()), int(entryStartY.get()), int(entryEndX.get()), int(entryStartY.get()), width=3, fill=entryColor.get())
    canvas.create_line(int(entryEndX.get()), int(entryStartY.get()), int(entryEndX.get()), int(entryEndY.get()), width=3, fill=entryColor.get())
    canvas.create_line(int(entryEndX.get()), int(entryEndY.get()), int(entryStartX.get()), int(entryEndY.get()), width=3, fill=entryColor.get())
    canvas.create_line(int(entryStartX.get()), int(entryEndY.get()), int(entryStartX.get()), int(entryStartY.get()), width=3, fill=entryColor.get())

def circle(e):
    canvas.create_oval(int(entryStartX.get()), int(entryStartY.get()), int(entryEndX.get()), int(entryEndY.get()), width=3, fill=entryColor.get())

def line(e):
    canvas.create_line(int(entryStartX.get()), int(entryStartY.get()), int(entryEndX.get()), int(entryEndY.get()), width=3, fill=entryColor.get())

# Class

# --- GUI START ---
window = Tk()

window.title("")
window.geometry("1200x600")

# GUI.classes

# GUI.images

# GUI.ui
# GUI.ui.label
labelColor = Label(window, text="Enter a Color:")
labelStartX = Label(window, text="StartX:")
labelStartY = Label(window, text="StartY:")
labelEndX = Label(window, text="EndX:")
labelEndY = Label(window, text="EndY:")

# GUI.ui.button

# GUI.ui.entry
entryColor = Entry(window)
entryStartX = Entry(window)
entryStartY = Entry(window)
entryEndX = Entry(window)
entryEndY = Entry(window)

entryColor.insert(0, "black")
entryStartX.insert(0, "0")
entryStartY.insert(0, "0")
entryEndX.insert(0, "0")
entryEndY.insert(0, "0")

# GUI.ui.canvas
canvas = Canvas(window, width=1200, height=510, bg="white", highlightbackground="lightgray")

# GUI.ui.(element.place())
canvas.pack()
labelStartX.place(relx=0.02, rely=0.9, anchor=CENTER)
entryStartX.place(relx=0.1, rely=0.9, anchor=CENTER)
labelStartY.place(relx=0.02, rely=0.95, anchor=CENTER)
entryStartY.place(relx=0.1, rely=0.95, anchor=CENTER)
labelEndX.place(relx=0.2, rely=0.9, anchor=CENTER)
entryEndX.place(relx=0.28, rely=0.9, anchor=CENTER)
labelEndY.place(relx=0.2, rely=0.95, anchor=CENTER)
entryEndY.place(relx=0.28, rely=0.95, anchor=CENTER)
labelColor.place(relx=0.38, rely=0.9, anchor=CENTER)
entryColor.place(relx=0.48, rely=0.9, anchor=CENTER)
Entry(window).place(relx=0.58, rely=0.9, anchor=CENTER)

# GUI.ui.keyevents
window.bind("<r>", rectangle)
window.bind("<c>", circle)
window.bind("<l>", line)

# --- GUI END --

window.mainloop()