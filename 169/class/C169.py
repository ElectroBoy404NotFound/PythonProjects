# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:26:11 2022

@author: elect
"""

# Imports
from tkinter import *

# Variables

# Function

# Classes
class Elements:
    def __init__(self, window):
        self.__window = window
        print("classElements __init__ has been triggered")
    
    def createNewElements(self):
        Label(self.__window, text="A new Label has been created using class", fg="red").pack()
        Button(self.__window, text=" Button ", command=self.__printMessage).pack(padx=20, pady=10)
        
    def __printMessage(self):
        messagebox.showinfo("Hi!", "You Clicked the button that was made in a class! (A python classroom!)")
    
# --- GUI START ---
window = Tk()

window.title("Classes")
window.geometry("900x600")
window.configure(background="white")

# GUI.images

# GUI.ui
# GUI.ui.classes
objectelementsObject = Elements(window=window)

# GUI.ui.label

# GUI.ui.button
buttonCreate = Button(window, text="Click to create a \"Label\" and a \"Button\" using a Class!", command=objectelementsObject.createNewElements)

# GUI.ui.(element.place())
buttonCreate.pack()

# --- GUI END --

window.mainloop()