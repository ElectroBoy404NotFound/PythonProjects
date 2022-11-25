# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 11:18:29 2022

@author: elect
"""

# Imports
import os, sys

from tkinter import Button, Tk, Text, Label, Entry, CENTER, END
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from bs4 import BeautifulSoup

# Variables
strFileName = ""
strRunFileName = ""

# Function
def shortcutTrigger(event):
    if event.keysym == 'o':
        openFile()
    if event.keysym == 's':
        saveFile()
    if event.keysym == 'q':
        exitIDE()
    if event.keysym == 'r':
        runFile()
    if event.keysym == 'b':
        html_doc = textFileContent.get(1.0, END)
        textFileContent.delete(1.0, END)
        textFileContent.insert(END, BeautifulSoup(html_doc).prettify())

def openFile():
    global strFileName
    textFileContent.delete(1.0, END)
    entryFileName.delete(0, END)
    strTextFile = filedialog.askopenfilename(title="Open File in PyIDE++", filetypes=[("HTML Files", "*.html"), ("CSS", "*.css"), ("Javascript","*.js"), ("All Files", "*.*")])
    entryFileName.insert(END, strTextFile)
    window.title("PyPad++ - " + strTextFile)
    fileInputFile = open(strTextFile, 'r')
    textFileContent.insert(END, fileInputFile.read())
    fileInputFile.close()

def saveFile():
    strFileName = entryFileName.get()
    if strFileName == "":
        strFileName = filedialog.askopenfilename(title="Open File in PyIDE++", filetypes=[("HTML Files", "*.html"), ("CSS", "*.css"), ("Javascript","*.js"), ("All Files", "*.*")])
    try:
        fileSaveFile = open(strFileName, "w")
    except FileNotFoundError:
        strFileName = filedialog.askopenfilename(title="Open File in PyIDE++", filetypes=[("HTML Files", "*.html"), ("CSS", "*.css"), ("Javascript","*.js"), ("All Files", "*.*")])
        fileSaveFile = open(strFileName, "w")
    fileSaveFile.write(textFileContent.get(1.0, END))
    fileSaveFile.close()
    messagebox.showinfo("Save", "Successfully saved " + strFileName)

def runFile():
    strFileName = entryFileName.get()
    if strFileName == "":
        strFileName = filedialog.askopenfilename(title="Open File in PyIDE++", filetypes=[("HTML Files", "*.html"), ("CSS", "*.css"), ("Javascript","*.js"), ("All Files", "*.*")])
    try:
        fileSaveFile = open(strFileName, "w")
    except FileNotFoundError:
        strFileName = filedialog.askopenfilename(title="Open File in PyIDE++", filetypes=[("HTML Files", "*.html"), ("CSS", "*.css"), ("Javascript","*.js"), ("All Files", "*.*")])
        fileSaveFile = open(strFileName, "w")
    fileSaveFile.write(textFileContent.get(1.0, END))
    fileSaveFile.close()
    
    global strRunFileName
    if strRunFileName == "":
        strRunFileName = filedialog.askopenfilename(title="Open File in PyIDE++", filetypes=[("HTML Files", "*.html"), ("CSS", "*.css"), ("Javascript","*.js"), ("All Files", "*.*")])
    os.startfile(strRunFileName)

def exitIDE():
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

# GUI.shortcuts
window.bind('<Control-Key>', shortcutTrigger)

# --- GUI END --

window.mainloop()