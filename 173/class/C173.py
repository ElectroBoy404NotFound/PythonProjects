# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:18:03 2022

@author: elect
"""

# Imports

# Variables

# Function

# Classes
class Parent():
    def __init__(self):
        pass
    
    def menu(self, dish):
        if dish == "burger":
            print("You can add the following toppings")
            print("Cheese (cheese) | Jalapeno (jalapeno)")
        elif dish == "iced_americano":
            print("You can add the following toppings")
            print("Chocolate flavour (chocolate) | Caramel flavour (caramel)")
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
                print("Your order total is 200USD")
            elif strAddon == "caramel":
                print("Your order total is 210USD")
            elif strAddon == "none":
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
            print("More Chocolate | More Milk")
        else:
            Parent.menu(self, self.__strDish)

    def finalAmount(self, strExtra):
        if self.__strDish == "ChocolateMilk":
            if strExtra == "chocolate":
                print("Your order total is 300USD")
            elif strExtra == "milk":
                print("Your order total is 310USD")
            else:
                print("Please enter a valid Extra")
                print("You can add the following extras:")
                print("More Chocolate | More Milk")
        else:
            Parent.finalAmount(self, strExtra)

# Main Code
child1Object = Child1("burger")
child2Object = Child2("burger", "cheese")
child3Object = Child3("ChocolateMilk")

child1Object.menu()
child2Object.menu()
child3Object.menu()

child1Object.finalAmount("cheese")
child2Object.finalAmount()
child3Object.finalAmount("chocolate")
