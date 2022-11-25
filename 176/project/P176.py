# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:19:16 2022

@author: elect
"""

# Imports
import speedtest
import matplotlib.pyplot as pyplot
import time

listSpeedsUp = []
listSpeedsDown = []

for i in range(5):
    sp = speedtest.Speedtest()
    listSpeedsUp.append(round(sp.upload() / 1000000, 2))
    listSpeedsDown.append(round(sp.download()/ 1000000, 2))
    time.sleep(60)

pyplot.plot([1, 2, 3, 4, 5], listSpeedsDown, label="Download Speed")
pyplot.title('Speed')
pyplot.plot([1, 2, 3, 4, 5], listSpeedsUp, label="Upload Speed")
pyplot.legend()
pyplot.show()