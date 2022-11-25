# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:47:34 2022

@author: elect
"""

# Imports
from tkinter import Tk, Button, Label, CENTER, filedialog
from PIL import ImageTk, Image

# Variables

# Function

# --- GUI START ---
window = Tk()

window.title("IGTech Image Viewer V1.0.0")
window.geometry("640x480")
window.configure(background="black")

# GUI.images

# GUI.ui
# GUI.ui.label
labelHeading = Label(window, font=("courier", 24, "bold"), text="IGTech Image Viewer", background="black", foreground="yellow")
labelImageTitle = Label(window, font=("normal", 10), text="Viewing: None", background="black", foreground="white")
labelImage = Label(window)

# GUI.ui.button
buttonOpenImage = Button(window, text="Open Image")

# GUI.ui.(element.place())
labelHeading.place(relx=0.5, rely=0.1, anchor=CENTER)
labelImageTitle.place(relx=0.5, rely=0.28, anchor=CENTER)

# --- GUI END --

window.mainloop()