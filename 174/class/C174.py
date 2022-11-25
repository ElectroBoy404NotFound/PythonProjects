# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 11:11:51 2022

@author: elect
"""

# Imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Variables
listAddons = []

# Function
def checkAddons():
    pass
def finalAmount():
    pass
def onPersonSelect():
    dropdownPerson.place_forget()
    labelSelectAddon.place(relx=0.08, rely=0.5, anchor=CENTER)
    buttonAmount.place(relx=0.055, rely=0.6, anchor=CENTER)
    labelFinalAmount.place(relx=0.2, rely=0.75, anchor=CENTER)
    labelSelectDish.place(relx=0.06, rely=0.2, anchor=CENTER)
    buttonAddons.place(relx=0.06, rely=0.3, anchor=CENTER)

# Classes
class Parent():
    __listDishes = ["burger", "iced_americano"]
    def __init__(self):
        pass
    
    def menu(self, dish):
        if dish == "burger":
            print("You can add the following toppings")
            print("Cheese (cheese) | Jalapeno (jalapeno) | None (none)")
            listAddons = ["cheese", "jalapeno", "none"]
        elif dish == "iced_americano":
            print("You can add the following toppings")
            print("Chocolate flavour (chocolate) | Caramel flavour (caramel) | None (none)")
            listAddons = ["chocolate", "caramel", "none"]
        else:
            print("Please enter a valid dish")
    
    def finalAmount(self, strDish, strAddon):
        if strDish == "burger": 
            if strAddon == "cheese":
                print("Your order total is 300USD")
            elif strAddon == "jalapeno":
                print("Your order total is 350USD")
            elif strAddon == "none":
                print("Your order total is 250USD")
            else:
                print("Please enter a valid addon")
        elif strDish == "iced_americano":
            if strAddon == "chocolate":
                labelFinalAmount['text'] = "Your order total is 200USD"
                print("Your order total is 200USD")
            elif strAddon == "caramel":
                labelFinalAmount['text'] = "Your order total is 210USD"
                print("Your order total is 210USD")
            elif strAddon == "none":
                labelFinalAmount['text'] = "Your order total is 180USD"
                print("Your order total is 180USD")
            else:
                print("Please enter a valid addon")
        else:
            print("Please enter a valid dish")

class Child1(Parent):
    def __init__(self, strDish):
        self.__strDish = strDish
    
    def menu(self):
        Parent.menu(self, self.__strDish)

    def finalAmount(self, strTopping):
        Parent.finalAmount(self, self.__strDish, strTopping)

class Child2(Parent):
    def __init__(self, strDish, strDishAddon):
        self.__strDish = strDish
        self.__strDishAddon = strDishAddon
    
    def menu(self):
        print("Ordered items cannot be changed")
    
    def finalAmount(self):
        Parent.finalAmount(self, self.__strDish, self.__strDishAddon)

class Child3(Parent):
    def __init__(self, strDish):
        self.__strDish = strDish
    
    def menu(self):
        if self.__strDish == "ChocolateMilk":
            print("You can add the following extras:")
            print("More Chocolate (chocolate) | More Milk (milk) | None (none")
            listAddons = ["chocolate", "milk", "none"]
        else:
            Parent.menu(self, self.__strDish)

    def finalAmount(self, strExtra):
        if self.__strDish == "ChocolateMilk":
            if strExtra == "chocolate":
                print("Your order total is 300USD")
                labelFinalAmount['text'] = "Your order total is 300USD"
            elif strExtra == "milk":
                print("Your order total is 310USD")
                labelFinalAmount['text'] = "Your order total is 310USD"
            elif strExtra == "none":
                labelFinalAmount['text'] = "Your order total is 295USD"
            else:
                print("Please enter a valid Extra")
                print("You can add the following extras:")
                print("More Chocolate (chocolate) | More Milk (milk) | None (none)")
                listAddons = ["chocolate", "milk", "none"]
        else:
            Parent.finalAmount(self, strExtra)

# Non-GUI Objects

# --- GUI START ---
window = Tk()

window.title("RDonalds")
window.geometry("900x500")
window.configure(background="white")

# GUI.images
labelBurger = Label(window)
labelBurger['image'] = ImageTk.PhotoImage(Image.open("assets/burger1.png"))

# GUI.ui
# GUI.ui.label
labelHeading = Label(window, text="RDonalds", font=("times", 40, "bold"), fg="Orange")

labelSelectDish = Label(window, text="Select Dish", font=("times", 15))
labelSelectAddon = Label(window, text="Select Add-Ons", font=("times", 15))

labelFinalAmount = Label(window, font=("times", 15, "bold"))

# GUI.ui.dropdown
stringvarDropdownValue = StringVar(value="Parent")
dropdownPerson = OptionMenu(window, stringvarDropdownValue, ["Parent", "Child", "Child2", "Child3"], command=onPersonSelect)

# GUI.ui.button
buttonAddons = Button(window, text="Check Add-Ons", command=checkAddons, fg="white", bg="blue")
buttonAmount = Button(window, text="Final Amount", command=finalAmount, fg="white", bg="blue")

# GUI.ui.(element.place())
labelHeading.place(relx=0.12, rely=0.1, anchor=CENTER)
labelBurger.place(relx=0.7, rely=0.5, anchor=CENTER)
dropdownPerson.place(relx=0.5, rely=0.5, anchor=CENTER)

# --- GUI END --

window.mainloop()