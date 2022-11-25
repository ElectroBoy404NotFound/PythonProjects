# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:20:00 2022

@author: elect
"""

# Imports

# Variables

# Function
def main():
    historyinspaceSpace = HistoryInSpace()
    historyinspaceSpace.year2008()
    historyinspaceSpace.year2011()
    
    historyinmedical = HistoryInMedical()
    historyinmedical.year2008()
    historyinmedical.year2011()
    
    historyinsports = HistoryInSports()
    historyinsports.year2008()
    historyinsports.year2011()

# Classes
class HistoryInSpace():
    def year2008(self):
        print("\n", "Events happened in space (2008 Edition)")
        print("India launched to space")
    
    def year2011(self):
        print("\n", "Events happened in space (2011 Edition)")
        print("History: Nothing happened in space in 2011")
        print("Mr.Python: No, Everything happened in python")
        print("History: We are talking about space history")
        
class HistoryInMedical():
    def year2008(self):
        print("\n", "Events happened in medical (2008 Edition)")
        print("Dec.8, final results of a malaria vaccine that shows promise hit international")
        
    def year2011(self):
        print("\n", "Events happened in medical (2011 Edition)")
        print("History: No events happened in medical in 2011")
        print("Mr.Python: No, Everything happened in python")
        print("History: We are talking about medical history, not python history")

class HistoryInSports():
    def year2008(self):
        print("\n", "Events happened in sports (2008 Edition)")
        print("His gold medal remaing asjdhasduagyuds")
        
    def year2011(self):
        print("\n", "Events happened in sports (2011 Edition)")
        print("History: No events happened in sports in 2011")
        print("Mr.Python: No, Everything happened in python")
        print("History: WE ARE TALKING ABOUT SPORTS HISTORY, NOT PYTHON HISTORY!!!")

# -- END --
if __name__ == "__main__":
    main()