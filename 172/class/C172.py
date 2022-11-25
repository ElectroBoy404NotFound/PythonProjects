# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:16:29 2022

@author: elect
"""

# Classes
class Doctor:
    def __init__(self):
        print("Time is class Doctor")
        
    def BMI(self, weight, height):
        print("Your BMI is " + str(weight / (height * height)))
    
    def heartrate(self, heartrate):
        if(heartrate > 60 and heartrate < 100):
            print("Your heartrate is normal")
        else:
            print("Your heartrate is not normal, please see a doctor")

class Paitent(Doctor):
    def __init__(self, pstrPaitentName, pintWeight, pintHeight, pintHeartRate):
        self.__strPaitentName = pstrPaitentName
        self.__intWeight = pintWeight
        self.__intHeight = pintHeight
        self.__intHeartRate = pintHeartRate
        
    def healthCheck(self):
        print("Paitent Name: ", self.__strPaitentName)
        Doctor.BMI(self, self.__intWeight, self.__intHeight)
        Doctor.heartrate(self, self.__intHeartRate)
        
# Main code
paitent1 = Paitent("Michael", 30, 0.9144, 80)
paitent2 = Paitent("Jessica", 40, 1, 120)

paitent1.healthCheck()
paitent2.healthCheck()