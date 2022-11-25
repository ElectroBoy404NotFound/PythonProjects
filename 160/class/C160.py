# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 11:18:29 2022

@author: elect
"""

# Imports
from tkinter import *
from PIL import ImageTk, Image

# Variables
file = None

# Function
def openFile():
    global file
    if file != None:
        file.close()
    file = open(entryFileName.get(), "r+")
    textFileContent.delete(1.0, END)
    textFileContent.insert('end', file.read())

def saveFile():
    global file
    if file == None:
        file = open(entryFileName.get(), "w+")
    file.seek(0)
    file.writelines(textFileContent.get(1.0, END))

def exitIDE():
    if file != None:
        file.close()
    window.destroy()
    sys.exit(0)

# --- GUI START ---
window = Tk()

window.title("PyPad++ v1.0.0")
window.geometry("650x650")
window.minsize(650, 650)
window.maxsize(650, 650)
window.configure(background="white")

# GUI.images
imageOpen = ImageTk.PhotoImage(Image.open("assets/open.png"))
imageSave = ImageTk.PhotoImage(Image.open("assets/save.png"))
imageClose = ImageTk.PhotoImage(Image.open("assets/exit.jpg"))

# GUI.ui
buttonOpen = Button(master=window, image=imageOpen, text="Open File", command=openFile)
buttonSave = Button(master=window, image=imageSave, text="Save File", command=saveFile)
buttonExit = Button(master=window, image=imageClose, text="Exit", command=exitIDE)
labelFileName = Label(master=window, text="Name")
entryFileName = Entry(master=window)
textFileContent = Text(master=window, height=35, width=80)

buttonOpen.place(relx=0.05, rely=0.03, anchor=CENTER)
buttonSave.place(relx=0.1, rely=0.03, anchor=CENTER)
buttonExit.place(relx=0.15, rely=0.03, anchor=CENTER)
labelFileName.place(relx=0.28, rely=0.03, anchor=CENTER)
entryFileName.place(relx=0.46, rely=0.03, anchor=CENTER)
textFileContent.place(relx=0.5, rely=0.55, anchor=CENTER)

# --- GUI END --

window.mainloop()