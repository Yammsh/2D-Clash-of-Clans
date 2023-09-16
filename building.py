from colorama import Fore, Back, Style
from village import *



class Building():
    def isDestroyed(self):
        if(self.hitpoint<=0):
            return True
        else: 
            return False

    
    
class Townhall(Building):
    def __init__(self,topleft,topright):
        self.hitpoint = 200
        self.initial_health = 200
        self.topleft = topleft
        self.topright = topright

    def colorChange(self):
        change = (self.hitpoint)/self.initial_health * 100
        change = int(change)

        if(change >= 20 and change <= 50):
            return Back.LIGHTMAGENTA_EX
        elif(change >= 0 and change <= 20):
            return Back.RED
        else: return Back.BLUE


class Huts(Building):
    def __init__(self,row,column):
        self.hitpoint = 100
        self.initial_health = 100
        self.row = row
        self.column = column
    
    def colorChange(self):
        change = (self.hitpoint)/self.initial_health * 100
        change = int(change)

        if(change >= 20 and change <= 50):
            return Back.LIGHTMAGENTA_EX
        elif(change >= 0 and change <= 20):
            return Back.RED
        else: return Back.CYAN



class Wall(Building): 
    def __init__(self,row,column):
        self.hitpoint = 100
        self.initial_health = 100
        self.row = row
        self.column = column

    def colorChange(self):
        change = (self.hitpoint)/self.initial_health * 100
        change = int(change)

        if(change >= 20 and change <= 50):
            return Back.LIGHTMAGENTA_EX
        elif(change >= 0 and change <= 20):
            return Back.RED
        else: return Back.YELLOW



    



         
