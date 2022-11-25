# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:47:34 2022

@author: elect
"""

# Imports
import sys

from tkinter import Tk, Button, Label, CENTER, filedialog, Menu
from PIL import ImageTk, Image

# Variables
imageOpenImage = None

# Function
def shortcutTrigger(event):
    if event.keysym == 'o':
        openImage()
    if event.keysym == 's':
        saveImage()
    if event.keysym == 'r':
        rotateImage()
        
def openImage():
    global imageOpenImage
    strImageFile = filedialog.askopenfilename(title="IGTech Image Viewer V1.0.0", filetypes=[("Image Files", "*.jpg, *.img, *.ico, *.png"), ("All Files", "*.*")])
    imageOpenImage = Image.open(strImageFile)
    image = ImageTk.PhotoImage(imageOpenImage)
    labelImage['image'] = image

def saveImage():
    None
    
def rotateImage():
    global imageOpenImage, image
    if imageOpenImage != None:
        imageOpenImage = imageOpenImage.rotate(90)
        image = ImageTk.PhotoImage(imageOpenImage)
        labelImage['image'] = image
    
def exit():
    window.destroy()
    window.quit()
    sys.exit(0)

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

# GUI.ui.menubar
menubarMainBar = Menu(window, background="#ff8000", foreground="black", activebackground='white', activeforeground='black')

menubarMainBar.add_command(label="Open Image (CTRL+O)", command=openImage)
menubarMainBar.add_command(label="Save Image (CTRL+S)", command=saveImage)
menubarMainBar.add_command(label="Rotate Image (CTRL+R)", command=rotateImage)
menubarMainBar.add_command(label="Exit (ALT+F4)", command=exit)

window.config(menu=menubarMainBar)

# GUI.ui.(element.place())
labelHeading.place(relx=0.5, rely=0.1, anchor=CENTER)
labelImageTitle.place(relx=0.5, rely=0.28, anchor=CENTER)
labelImage.place(relx=0.5, rely=0.6, anchor=CENTER)

# GUI.other
window.bind('<Control-Key>', shortcutTrigger)

# --- GUI END --

window.mainloop()