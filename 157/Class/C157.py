# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 09:24:48 2022

@author: elect
"""

# Imports
from tkinter import *
from PIL import ImageTk, Image

import random

# Variables
intPlayer1Score = 0
intPlayer2Score = 0

# Functions
def player1():
    global intPlayer1Score
    intRandomNo = random.randint(1, 6)
    labelRandomDiceLabel["text"] = "Player 1 Dice Random Number : " + str(intRandomNo)
    intPlayer1Score = intPlayer1Score + intRandomNo
    labelPlayer1Score["text"] = str(intPlayer1Score)
    
def player2():
    global intPlayer2Score
    intRandomNo = random.randint(1, 6)
    labelRandomDiceLabel["text"] = "Player 2 Dice Random Number : " + str(intRandomNo)
    intPlayer2Score = intPlayer2Score + intRandomNo
    labelPlayer2Score["text"] = str(intPlayer2Score)
    
# --- GUI START ---

# GUI.window
window = Tk()

window.title("Endless Dice Game")
window.geometry("600x400")

window.configure(background="yellow2")

# GUI.dice
labelRandomDiceLabel = Label(master=window, text="0", bg="chocolate1", fg="white")

imageDice = ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

labelRandomDiceLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

# GUI.Player1
labelPlayer1 = Label(master=window, text="Player 1", bg="royal blue", fg="white")
labelPlayer1Score = Label(master=window, text="0", bg="royal blue", fg="white")

labelPlayer1.place(relx=0.1, rely=0.3, anchor=CENTER)
labelPlayer1Score.place(relx=0.1, rely=0.4, anchor=CENTER)

buttonPlayer1 = Button(window, image=imageDice, command=player1)
buttonPlayer1.place(relx=0.1, rely=0.6 , anchor=CENTER)

# GUI.Player2
labelPlayer2 = Label(master=window, text="Player 2", bg="royal blue", fg="white")
labelPlayer2Score = Label(master=window, text="0", bg="royal blue", fg="white")

labelPlayer2.place(relx=0.9, rely=0.3, anchor=CENTER)
labelPlayer2Score.place(relx=0.9, rely=0.4, anchor=CENTER)

buttonPlayer2 = Button(window, image=imageDice, command=player2)
buttonPlayer2.place(relx=0.9, rely=0.6 , anchor=CENTER)

# --- GUI END ---
window.mainloop()