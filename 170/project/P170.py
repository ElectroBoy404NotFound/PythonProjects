# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:53:41 2022

@author: elect
"""

from tkinter import *
root=Tk()
root.geometry("500x500")
class Grade_3():
    def __init__(self,language_arts,mathematics):
        self.language_arts=language_arts
        self.mathematics=mathematics
    def percentage(self):
        percent=self.language_arts+self.mathematics
        percent=percent/2
        label_3['text']=percent
class Grade_5():
    def __init__(self,language_arts,mathematics,social_studies):
        self.language_arts=language_arts
        self.mathematics=mathematics
        self.social_studies=social_studies
    def percentage(self):
        percent=self.language_arts+self.mathematics+self.social_studies
        percent=percent/3
        label_5['text']=percent
class Grade_10():
    def __init__(self,language_arts,mathematics,foreign_language,social_studies):
        self.language_arts=language_arts
        self.mathematics=mathematics
        self.foreign_language=foreign_language
        self.social_studies=social_studies
    def percentage(self):
        percent=self.social_studies+self.language_arts+self.mathematics+self.foreign_language
        percent=percent/4
        label_10['text']=percent
g3=Grade_3(40,50)
btn_3=Button(root,text="Grade 3",command=g3.percentage)
btn_3.place(relx=0.5,rely=0.1,anchor=CENTER)
label_3=Label(root)
label_3.place(relx=0.5,rely=0.2,anchor=CENTER)
g5=Grade_5(40,50,90)
btn_5=Button(root,text="Grade 5",command=g5.percentage)
btn_5.place(relx=0.5,rely=0.3,anchor=CENTER)
label_5=Label(root)
label_5.place(relx=0.5,rely=0.4,anchor=CENTER)
g10=Grade_10(40,50,90,70)
btn_10=Button(root,text="Grade 10",command=g10.percentage)
btn_10.place(relx=0.5,rely=0.5,anchor=CENTER)
label_10=Label(root)
label_10.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()