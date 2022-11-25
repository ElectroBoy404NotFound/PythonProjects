# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:13:30 2022

@author: elect
"""

# Imports
from tkinter import *
from PIL import ImageTk, Image

# Variables

# Function
def getFlag(cname):
    try:
        return dictionaryCountryAndFlag[cname]
    except KeyError:
        messagebox.showinfo("Error!", "Sorry, we are unable to find the country \"" + cname + "\" in our database, plsease contact us.\nemail: electroboy404notfound@gmail.com")
        return None
    except:
        messagebox.showinfo("Error!", "Sorry, an unknown error has occured, plsease contact us.\nemail: electroboy404notfound@gmail.com")
        return None

def getAndSetFlag():
    labelFlagImage["image"] = getFlag(entryCountry.get())

# --- GUI START ---
window = Tk()

window.title("Country Name to Map Convertor")
window.geometry("600x400")
window.configure(background="lightblue")

# GUI.images
imageIndia = ImageTk.PhotoImage(Image.open("India.jpg"))
imageAmerica = ImageTk.PhotoImage(Image.open("America.jpg"))
imageAustralia = ImageTk.PhotoImage(Image.open("Australia.png"))
imagePhilippines = ImageTk.PhotoImage(Image.open("Philippines.png"))
imageJapan = ImageTk.PhotoImage(Image.open("Japan.jpg"))

dictionaryCountryAndFlag = { "India" : imageIndia, 
                    "America" : imageAmerica,
                    "Australia" : imageAustralia,
                    "Philippines" : imagePhilippines,
                    "Japan" : imageJapan}

# GUI.UI
entryCountry = Entry(master=window)
buttonConvert = Button(master=window, text="Convert", bg="green", command=getAndSetFlag)
labelFlagImage = Label(master=window)

entryCountry.place(relx=0.5, rely=0.1, anchor=CENTER)
buttonConvert.place(relx=0.5, rely=0.2, anchor=CENTER)
labelFlagImage.place(relx=0.5, rely=0.6, anchor=CENTER)

# --- GUI END --

window.mainloop()