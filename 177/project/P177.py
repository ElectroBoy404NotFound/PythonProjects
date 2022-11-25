# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 18:38:13 2022

@author: elect
"""

# Imports
from tkinter import *
from PIL import ImageTk, Image

# Variables

# Functions
def checkUser():
    usersUsers.checkUser(BasicUser(entryUsername.get(), entryPassword.get(), entryCaptcha.get()))

# Classes
class BasicUser():
    def __init__(self, pstrUsername, pstrPassword, pstrCaptcha):
        self.__strUsername = pstrUsername
        self.__strPassword = pstrPassword
        self.__strCaptcha = pstrCaptcha
        
    def getUsername(self):
        return self.__strUsername
    def getPassword(self):
        return self.__strPassword
    def getCaptcha(self):
        return self.__strCaptcha
    def getSelf(self):
        return self

class Users(BasicUser):
    __listUsers = {}
    
    def __init__(self):
        BasicUser.__init__(BasicUser, "AdminUser53922", "AdminPassword@123", "random.randint()")
        self.__listUsers.update({self.getUsername(): [self.getUsername(), self.getPassword(), self.getCaptcha()]})

    def addUser(self, basicuserUser):
        self.__listUsers.update({basicuserUser.getUsername(): [basicuserUser.getUsername(), basicuserUser.getPassword(), basicuserUser.getCaptcha()]})
        
    def printUsers(self):
        for i in self.__listUsers:
            print(i, ":", self.__listUsers.get(i))
    def checkUser(self, BasicUser):
        

usersUsers = Users()

usersUsers.addUser(BasicUser("TheUser", "theuserpassword", "Meow"))

# --- GUI START ---
window = Tk()

window.title("Operl Attendence")
window.geometry("500x400")
window.configure(background="white")

# GUI.images
imageLogo = Label(master=window, image=ImageTk.PhotoImage(Image.open("./logo.jpg")))

# GUI.ui
# GUI.ui.label
labelNameEntry = Label(master=window, text="Name: ")
labelPasswordEntry = Label(master=window, text="Password: ")
labelCaptchaEntry = Label(master=window, text="Captcha: ")

# GUI.ui.entry
entryUsername = Entry(window)
entryPassword = Entry(window)
entryCaptcha = Entry(window)

# GUI.ui.button
buttonLogin = Button(window, text="Check Login", command=checkUser)

# GUI.ui.(element.place())
imageLogo.place(relx=0.5, rely=0.2, anchor=CENTER)
labelNameEntry.place(relx=0.3, rely=0.4, anchor=CENTER)
entryUsername.place(relx=0.5, rely=0.4, anchor=CENTER)
labelPasswordEntry.place(relx=0.3, rely=0.5, anchor=CENTER)
entryPassword.place(relx=0.5, rely=0.5, anchor=CENTER)
labelCaptchaEntry.place(relx=0.3, rely=0.6, anchor=CENTER)
entryCaptcha.place(relx=0.5, rely=0.6, anchor=CENTER)

# --- GUI END --

window.mainloop()