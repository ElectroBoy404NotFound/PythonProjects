# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 19:39:57 2022

@author: elect
"""

# Imports
from tkinter import Tk, Radiobutton, StringVar, Label, Button, messagebox

# Variables

# Function
def getScore():
    score = 0
    if stringVarQ1.get() == "yes":
        score = 20
    if stringVarQ2.get() == "yes":
        score = score + 20
    if stringVarQ3.get() == "yes":
        score = score + 20
    if stringVarQ4.get() == "yes":
        score = score + 20
    if stringVarQ5.get() == "yes":
        score = score + 20
    
    if score <= 20:
        messagebox.showinfo("Report", "You don't need to go to a doctor.")
    elif score <= 40:
        messagebox.showwarning("Report", "You might need to go to a doctor.")
    else:
        messagebox.showerror("Report", "You need to go to a doctor.")

# --- GUI START ---
window = Tk()

window.title("Fever Report")
window.configure(background="white")

# GUI.ui

stringVarQ1 = StringVar(value="0")
stringVarQ2 = StringVar(value="0")
stringVarQ3 = StringVar(value="0")
stringVarQ4 = StringVar(value="0")
stringVarQ5 = StringVar(value="0")

Label(window, text="Do you exprince shortness of breath during routine activities?").pack()
Radiobutton(window, text="yes", variable=stringVarQ1, value="yes").pack()
Radiobutton(window, text="no", variable=stringVarQ1, value="no").pack()

Label(window, text="Do you have swelling in feet/ankles/legs (shoes fell thighter) or abdomen?").pack()
Radiobutton(window, text="yes", variable=stringVarQ2, value="yes").pack()
Radiobutton(window, text="no", variable=stringVarQ2, value="no").pack()

Label(window, text="Do you feel any of the following symptoms - confusion, disorientation or loss memory?").pack()
Radiobutton(window, text="yes", variable=stringVarQ3, value="yes").pack()
Radiobutton(window, text="no", variable=stringVarQ3, value="no").pack()

Label(window, text="Do you experience shortness of breath while at rest/lying down?").pack()
Radiobutton(window, text="yes", variable=stringVarQ4, value="yes").pack()
Radiobutton(window, text="no", variable=stringVarQ4, value="no").pack()

Label(window, text="Do you experience persistent wheezing/choughing that produces white or pink blood tinged mucus?").pack()
Radiobutton(window, text="yes", variable=stringVarQ5, value="yes").pack()
Radiobutton(window, text="no", variable=stringVarQ5, value="no").pack()

Button(window, text="Click here to get report", command=getScore).pack()

# --- GUI END --

window.mainloop()