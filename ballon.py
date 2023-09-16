from village import Village
from colorama import Fore, Back, Style
import math
vil = Village(0)

class Ballon():
    def __init__(self,row,column):
        self.damage = 40
        self.hitpoint = 100
        self.initial_health = 100
        self.speed = 2
        self.row = row
        self.column = column
        self.steplength = 2
        self.limit = 6

    def colorChange(self):
        change = (self.hitpoint)/100 * 100
        change = int(change)

        if(change >= 20 and change <= 50):
            return Back.LIGHTCYAN_EX
        elif(change >= 0 and change <= 20):
            return Back.RED
        else: return Back.GREEN

    def move(self,vil):
        mini_x = 0 # minimum pair
        mini_y = 0
        dist = 10000000 # variable to find the minimum distance between barbarian and any building present
        
        if(len(vil.cannon)!=0 or len(vil.wizardTower)!=0):
            dist = 10000000
            for temp in vil.cannon:
                x = temp.row
                y = temp.column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= dist ):
                    dist = math.sqrt((x-self.row)**2 + (y-self.column)**2)
                    mini_x = x
                    mini_y = y 

            for temp in vil.wizardTower:
                x = temp.row
                y = temp.column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= dist ):
                    dist = math.sqrt((x-self.row)**2 + (y-self.column)**2)
                    mini_x = x
                    mini_y = y

        else:
            dist = 10000000
            for temp in vil.huts:
                x = temp.row
                y = temp.column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= dist ):
                    dist = math.sqrt((x-self.row)**2 + (y-self.column)**2)
                    mini_x = x
                    mini_y = y 

            # for townhall
            if(len(vil.townhall)!=0):
                temp_th = vil.townhall[0]
                for i in range(4):
                    for j in range(3):
                        if( math.sqrt((temp_th.topleft-self.row+i)**2 + (temp_th.topright-self.column+j)**2) <= dist ):
                            dist = math.sqrt((temp_th.topleft-self.row+i)**2 + (temp_th.topright-self.column+j)**2)
                            mini_x = temp_th.topleft+i
                            mini_y = temp_th.topright + j

        if(mini_x != self.row and abs(mini_x-self.row)+abs(mini_y - self.column)!=1):

            if(self.row < mini_x):

                for i in range(self.steplength):
                    if(self.row == mini_x):
                        break
                    else:
                        if(self.row+1 >= vil.rows):
                            return
                        self.row +=1
                
            
            elif(mini_x < self.row):

                for i in range(self.steplength):
                    if(self.row ==mini_x):
                        break
                    else:
                        if(self.row-1 < 0):
                            return
                        self.row -=1
                

        else:
            if(abs(mini_x-self.row)+abs(mini_y-self.column)==1): # troop has reached the desired position
                    if(vil.is_present[mini_x][mini_y]==1): # canon
                        for can in vil.cannon:
                            if (can.row == mini_x and can.column == mini_y):
                                can.hitpoint -= self.damage
                                if(can.isDestroyed()):
                                    vil.cannon.remove(can)
                                    vil.is_present[mini_x][mini_y] = 0
                                # else:
                                #     return
                                    # break

                    elif(vil.is_present[mini_x][mini_y]==2): # townhall
                        vil.townhall[0].hitpoint -= self.damage
                        if(vil.townhall[0].isDestroyed()):
                            for i in range(4):
                                for j in range(3):
                                    vil.is_present[10+i][24+j] = 0
                            vil.townhall.clear() 

                    elif(vil.is_present[mini_x][mini_y] == 3): #hut
                        for can in vil.huts:
                            if (can.row == mini_x and can.column == mini_y):
                                can.hitpoint -= self.damage
                                if(can.isDestroyed()):
                                    vil.huts.remove(can)
                                    vil.is_present[mini_x][mini_y] = 0
                                # else:
                                #     return
                                    # break

                    elif(vil.is_present[mini_x][mini_y] == 5): # wizardTower
                        for can in vil.wizardTower:
                            if (can.row == mini_x and can.column == mini_y):
                                can.hitpoint -= self.damage
                                if(can.isDestroyed()):
                                    vil.wizardTower.remove(can)
                                    vil.is_present[mini_x][mini_y] = 0
                                # else:
                                #     return
                                    # break

            else: # troop hasn't reached therefore we need to check if y<mini_column or not

                if(mini_y > self.column):
                        
                    for i in range(self.steplength):
                        if(self.column+1 == mini_y):
                            break
                        else:
                            if(self.column+1 >= vil.columns):
                                return
                            self.column +=1
                    
                
                elif(mini_y < self.column):
                            
                    for i in range(self.steplength):
                        if(self.column-1 == mini_y):
                            break
                        else:
                            if(self.column-1 < 0):
                                return
                            self.column -=1

    def rageSpell(self):
        self.damage *= 2
        self.steplength *= 2

    def healSpell(self):
        self.hitpoint = min(self.hitpoint*(1.5),self.initial_health)


            

             
