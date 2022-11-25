# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:46:48 2022

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
        self.__stringvarDropdownValue = StringVar()
        self.__stringvarDropdownValue.set("1")
        print("classElements __init__ has been triggered")
    
    def createNewElements(self, value):
        type = value
        if type == "label":
            Label(self.__window, text="A new Label has been created using class", fg="red").pack()
        if type == "button":
            Button(self.__window, text=" Button ", command=self.__buttonTrigger).pack(padx=20, pady=10)
        if type == "dropdown":
            OptionMenu(self.__window, self.__stringvarDropdownValue, *["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], command=self.__dropdownTrigger).pack()
    
    def __buttonTrigger(self):
        messagebox.showinfo("Hi!", "You Clicked the button made using a class!")
    
    def __dropdownTrigger(self, value):
        messagebox.showinfo("Hi!", "You Selected the value \"" + value + "\" in the Dropdown!")
    
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
#buttonCreate = Button(window, text="Click to create a \"Label\" and a \"Button\" using a Class!", command=objectelementsObject.createNewElements)

# GUI.ui.entry

# GUI.ui.dropdown
strvarStringVar = StringVar()
strvarStringVar.set("dropdown")
OptionMenu(window, strvarStringVar, *["dropdown", "button", "label"], command=objectelementsObject.createNewElements).pack()

# GUI.ui.(element.place())
#buttonCreate.pack()

# --- GUI END --

window.mainloop()