# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 11:27:39 2022

@author: elect
"""

class Citizen:
    def __init__(self, strName, intAge, strDOB, strIDNumber):
        self.__strName = strName;
        self.__intAge = intAge;
        self.__strDOB = strDOB;
        self.__strIDNumber = strIDNumber;
        
    def addCitizen(self):
        print("--CITIZEN INFO BEGIN--")
        print("Name:          " + self.__strName)
        print("Age:           " + str(self.__intAge))
        print("Date Of Birth: " + self.__strDOB)
        print("Citizen ID:    " + self.__strIDNumber)
        print("---CITIZEN INFO END---")
        print("Citizen Added.")
        
citizenJyothi = Citizen("Jyothi Jha", 44, "19-19-1919", "0001")
citizenNikunj = Citizen("Nikunj Chiluvuri", 12, "16-09-2010", "0003")

citizenJyothi.addCitizen()
citizenNikunj.addCitizen()