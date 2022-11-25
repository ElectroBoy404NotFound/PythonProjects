# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:13:51 2022

@author: elect
"""

# Imports
from tkinter import *
import random

# Functions
def changeBackground():
    stringColor = dictionaryColors["colour"][random.randint(0, 7)]
    print(stringColor)
    window.configure(background=stringColor)

# Variables
dictionaryColors = {"colour" : ["maroon1", "lawn green", "magenta2", "purple1", "springgreen2", "chocolate1", "deep pink", "cyan"]}

# --- GUI START ---
window = Tk()
window.title("Dictionary")
window.geometry("600x400")
    
buttonChangeBackground = Button(master=window, text="Change Background", command=changeBackground)
buttonChangeBackground.place(relx=0.5, rely=0.5, anchor=CENTER)

# --- GUI END ---

window.mainloop()