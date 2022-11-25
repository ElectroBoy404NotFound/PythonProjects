# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 18:24:34 2022

@author: elect
"""

import matplotlib.pyplot as ppl
import psutil
import sys

appnamelabel = []
appnamepercentagelist = []
count = 0
for process in psutil.process_iter():
    per = process.cpu_percent()
    name = process.name()
    if per > 0:
        count = count + 1
        if count <= 6:
            print("name: ", name, "; CPU usage", per)
            appnamelabel.append(name)
            appnamepercentagelist.append(per)
ppl.figure(figsize=(15, 7))
ppl.xlabel("Application")
ppl.ylabel("Usage")
ppl.bar(appnamelabel, appnamepercentagelist, width=0.6, color=("purple", "green", "red", "blue", "orange", "pink"))
ppl.show()