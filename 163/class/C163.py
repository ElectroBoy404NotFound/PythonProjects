# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 19:01:18 2022

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

Label(window, text="Do you have headache or sore throat?").pack()
Radiobutton(window, text="yes", variable=stringVarQ1, value="yes").pack()
Radiobutton(window, text="no", variable=stringVarQ1, value="no").pack()

Label(window, text="Is your body tempreture high?").pack()
Radiobutton(window, text="yes", variable=stringVarQ2, value="yes").pack()
Radiobutton(window, text="no", variable=stringVarQ2, value="no").pack()

Label(window, text="Are there any symptoms of eye redness?").pack()
Radiobutton(window, text="yes", variable=stringVarQ3, value="yes").pack()
Radiobutton(window, text="no", variable=stringVarQ3, value="no").pack()

Button(window, text="Click here to get report", command=getScore).pack()

# --- GUI END --

window.mainloop()