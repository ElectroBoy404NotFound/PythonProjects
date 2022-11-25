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
intPlayer1Score = 0
intPlayer2Score = 0

listPokemonHP = [200, 60, 100, 50, 50, 40, 70, 60, 70, 30, 70]

# Function
def player1():
    intPokemonNo = random.randint(0, 10)
    global intPlayer1Score
    randomPokemon = imglistPokemonList[intPokemonNo]
    intPlayer1Score = intPlayer1Score + listPokemonHP[intPokemonNo]
    labelRandomDice["image"] = randomPokemon
    labelPlayer1Score["text"] = str(intPlayer1Score)

def player2():
    intPokemonNo = random.randint(0, 10)
    global intPlayer2Score
    randomPokemon = imglistPokemonList[intPokemonNo]
    intPlayer2Score = intPlayer2Score + listPokemonHP[intPokemonNo]
    labelRandomDice["image"] = randomPokemon
    labelPlayer2Score["text"] = str(intPlayer2Score)

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
#imageButton = ImageTk.PhotoImage(Image.open("assets/button.jpg"))

imglistPokemonList = [imagePikachu, imageBulbasour, imageCharmender, imageSquirtle, imageRatata, imageNidoking, imageJigglypuff, imageMeowth, imagePersion, imageAbra, imageKadabra, imageIyvasour]

# GUI.player1
labelPlayer1 = Label(master=window, text="Player1", bg="red", fg="white")
labelPlayer1Score = Label(master=window, bg="royal blue", fg="white")

buttonPlayer1Play = Button(master=window, command=player1)
#buttonPlayer1Play["image"] = imageButton

labelPlayer1.place(relx=0.1, rely=0.3 , anchor=CENTER)
labelPlayer1Score.place(relx=0.1, rely=0.4, anchor=CENTER)
buttonPlayer1Play.place(relx=0.1, rely=0.6, anchor=CENTER)

# GUI.player2
labelPlayer2 = Label(master=window, text="Player2", bg="red", fg="white")
labelPlayer2Score = Label(master=window, bg="royal blue", fg="white")

buttonPlayer2Play = Button(master=window, command=player2)
#buttonPlayer2Play["image"] = imageButton

labelPlayer2.place(relx=0.9, rely=0.3 , anchor=CENTER)
labelPlayer2Score.place(relx=0.9, rely=0.4, anchor=CENTER)
buttonPlayer2Play.place(relx=0.9, rely=0.6, anchor=CENTER)

# GUI.dice
labelRandomDice = Label(master=window)

labelRandomDice.place(relx=0.5, rely=0.5, anchor=CENTER)

# --- GUI END --

window.mainloop()