# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:37:21 2022

@author: elect
"""

# Imports
from tkinter import *
from PIL import ImageTk, Image

# Variables

# Function
def adduser():
    usersUsers.addUser(BasicUser(entryUsername.get(), entryPassword.get()))
    labelUsers['text'] = usersUsers.getUsers()

# Classes
class BasicUser():
    def __init__(self, pstrUsername, pstrEmail):
        self.__strUsername = pstrUsername
        self.__strEmail = pstrEmail
        
    def getUsername(self):
        return self.__strUsername
    def getEmail(self):
        return self.__strEmail
    def getSelf(self):
        return self

class Users(BasicUser):
    __listUsers = {}
    
    def __init__(self):
        BasicUser.__init__(BasicUser, "AdminUser53922", "adminadamsir@eventmania.org")
        self.__listUsers.update({self.getEmail(): self.getUsername()})

    def addUser(self, basicuserUser):
        self.__listUsers.update({basicuserUser.getEmail(): basicuserUser.getUsername()})
        
    def printUsers(self):
        for i in self.__listUsers:
            print(i, ":", self.__listUsers.get(i))
    def getUsers(self):
        return self.__listUsers

usersUsers = Users()

# --- GUI START ---
window = Tk()

window.title("")
window.geometry("400x300")
window.configure(background="white")

# GUI.images

# GUI.ui
# GUI.ui.label
labelUsername = Label(window, text="Username: ")
labelPassword = Label(window, text="Email: ")
labelUsers = Label(window, text=usersUsers.getUsers())

# GUI.ui.button
buttonAddUser = Button(window, text="Add User", command=adduser)

# GUI.ui.entry
entryUsername = Entry(window)
entryPassword = Entry(window)

# GUI.ui.(element.place())
labelUsername.pack()
entryUsername.pack()
labelPassword.pack()
entryPassword.pack()
buttonAddUser.pack()
labelUsers.pack()
# --- GUI END --
window.mainloop()
