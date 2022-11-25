# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:25:43 2022

@author: elect
"""

import matplotlib.pyplot as pyplot
import psutil

dictonaryAppNameToUsage = {}

intCount = 0
for process in psutil.process_iter():
    intCount = intCount + 1
    if intCount <= 6:
        dictonaryAppNameToUsage.update({process.name: process.cpu_percent()})

intKeyMax = max(dictonaryAppNameToUsage, key=dictonaryAppNameToUsage.get)
intKeyMin = min(dictonaryAppNameToUsage, key=dictonaryAppNameToUsage.get)

intMaxApp = max(dictonaryAppNameToUsage.values())
intMinApp = max(dictonaryAppNameToUsage.values())

pyplot.figure(figsize=(15,8))
pyplot.xlabel("Min-Max CPU Consumption")
pyplot.ylabel("Usage")
maxminlist = [intMaxApp, intMinApp]
namelist = [intKeyMax, intKeyMin]
pyplot.bar(namelist, maxminlist, width=0.6, color=("blue", "red"))
pyplot.show()
