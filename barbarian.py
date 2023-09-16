from village import Village
from colorama import Fore, Back, Style
import math
vil = Village(0)

class Barbarian():
    def __init__(self,row,column):
        self.damage = 20
        self.hitpoint = 100
        self.initial_health = 100
        self.speed = 1
        self.row = row
        self.column = column
        self.steplength = 1

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
        

        for temp in vil.huts:
            x = temp.row
            y = temp.column
            if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= dist ):
                dist = math.sqrt((x-self.row)**2 + (y-self.column)**2)
                mini_x = x
                mini_y = y 

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
                    
        # for townhall
        if(len(vil.townhall)!=0):
            temp_th = vil.townhall[0]
            for i in range(4):
                for j in range(3):
                    if( math.sqrt((temp_th.topleft-self.row+i)**2 + (temp_th.topright-self.column+j)**2) <= dist ):
                        dist = math.sqrt((temp_th.topleft-self.row+i)**2 + (temp_th.topright-self.column+j)**2)
                        mini_x = temp_th.topleft+i
                        mini_y = temp_th.topright + j

        if(mini_x != self.row):

            if(self.row < mini_x):

                flgwall = 0
                for i in range(self.steplength):
                    if(vil.is_present[self.row+1][self.column]==4 or self.row == mini_x):
                        flgwall = 1
                        break
                    else:
                        if(self.row+1 >= vil.rows):
                            return
                        self.row +=1
                
                if(flgwall==1):
                    temp_pos = self.row+1
                    for wall in vil.walls:
                        if(wall.row == temp_pos and wall.column == self.column):
                            wall.hitpoint -= self.damage
                            if(wall.isDestroyed()):
                                vil.walls.remove(wall)
                                vil.is_present[temp_pos][self.column] = 0
                            else:
                                return
            
            elif(mini_x < self.row):

                flgwall = 0
                for i in range(self.steplength):
                    if(vil.is_present[self.row-1][self.column]==4 or self.row ==mini_x):
                        flgwall = 1
                        break
                    else:
                        if(self.row-1 < 0):
                            return
                        self.row -=1
                
                if(flgwall==1):
                    temp_pos = self.row-1
                    for wall in vil.walls:
                        if(wall.row == temp_pos and wall.column == self.column):
                            wall.hitpoint -= self.damage
                            if(wall.isDestroyed()):
                                vil.walls.remove(wall)
                                vil.is_present[temp_pos][self.column] = 0
                            else:
                                return

        else:
            if(abs(mini_y-self.column)==1): # troop has reached the desired position
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
                        
                    flgwall = 0
                    for i in range(self.steplength):
                        if(vil.is_present[self.row][self.column+1]==4 or self.column+1 == mini_y):
                            flgwall = 1
                            break
                        else:
                            if(self.column+1 >= vil.columns):
                                return
                            self.column +=1
                    
                    if(flgwall==1):
                        temp_pos = self.column+1
                        for wall in vil.walls:
                            if(wall.row == self.row and wall.column == temp_pos):
                                wall.hitpoint -= self.damage
                                if(wall.isDestroyed()):
                                    vil.walls.remove(wall)
                                    vil.is_present[self.row][temp_pos] = 0
                                else:
                                    return

                
                elif(mini_y < self.column):
                            
                    flgwall = 0
                    for i in range(self.steplength):
                        if(vil.is_present[self.row][self.column-1]==4 or self.column-1 == mini_y):
                            flgwall = 1
                            break
                        else:
                            if(self.column-1 < 0):
                                return
                            self.column -=1
                    
                    if(flgwall==1):
                        temp_pos = self.column-1
                        for wall in vil.walls:
                            if(wall.row == self.row and wall.column == temp_pos):
                                wall.hitpoint -= self.damage
                                if(wall.isDestroyed()):
                                    vil.walls.remove(wall)
                                    vil.is_present[self.row][temp_pos] = 0
                                else:
                                    return

                
    def rageSpell(self):
        self.damage *= 2
        self.steplength *= 2

    def healSpell(self):
        self.hitpoint = min(self.hitpoint*(1.5),self.initial_health)


            

             
