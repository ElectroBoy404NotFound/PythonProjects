# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 09:32:13 2022

@author: elect
"""

# Imports
from tkinter import *
from PIL import ImageTk, Image
import random

# Variables

# Function

# --- GUI START ---
window = Tk()

window.title("Endless Pokemon Game")
window.geometry("800x600")
window.configure(background="orange")

# GUI.images
imagePikachu = ImageTk.PhotoImage(Image.open("assets/pikachu.jpg"))
imageBulbasour = ImageTk.PhotoImage(Image.open("assets/bulbasour.jpg"))
imageCharmender = ImageTk.PhotoImage(Image.open("assets/charmender.jpg"))
imageSquirtle = ImageTk.PhotoImage(Image.open("assets/squirtle.jpg"))
imageRatata = ImageTk.PhotoImage(Image.open("assets/ratata.jpg"))
imageNidoking = ImageTk.PhotoImage(Image.open("assets/nidoking.jpg"))
imageJigglypuff = ImageTk.PhotoImage(Image.open("assets/jigglypuff.jpg"))
imageMeowth = ImageTk.PhotoImage(Image.open("assets/meowth.jpg"))
imagePersion = ImageTk.PhotoImage(Image.open("assets/persion.jpg"))
imageAbra = ImageTk.PhotoImage(Image.open("assets/abra.jpg"))
imageKadabra = ImageTk.PhotoImage(Image.open("assets/kadabra.jpg"))
imageIyvasour = ImageTk.PhotoImage(Image.open("assets/Iyvasour.jpg"))

# GUI.player1
labelPlayer1 = Label(master=window, text="Player1", bg="red", fg="white")
labelPlayer1Score = Label(master=window, bg="royal blue", fg="white")

labelPlayer1.place(relx=0.1, rely=0.3 , anchor=CENTER)
labelPlayer1Score.place(relx=0.1, rely=0.4, anchor=CENTER)

# GUI.player2
labelPlayer2 = Label(master=window, text="Player2", bg="red", fg="white")
labelPlayer2Score = Label(master=window, bg="royal blue", fg="white")

labelPlayer2.place(relx=0.9, rely=0.3 , anchor=CENTER)
labelPlayer2Score.place(relx=0.9, rely=0.4, anchor=CENTER)

# GUI.dice
labelRandomDice = Label(master=window)

labelRandomDice.place(relx=0.5, rely=0.5, anchor=CENTER)

# --- GUI END --

window.mainloop()