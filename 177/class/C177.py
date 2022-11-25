# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 18:07:19 2022

@author: elect
"""

class score():
    def __init__(self):
        self.__score = 1
    def updateScore(self):
        self.__score = self.__score + 1
        print(self.__score)
        
player = score()
player.__score = 100
player.updateScore()
player.updateScore()