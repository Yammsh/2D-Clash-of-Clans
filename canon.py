from village import *
import math

class Canon():
    def __init__(self,row,column):
        self.damage = 20
        self.row=row
        self.column=column
        self.hitpoint = 30
        self.radius = 4

    def colorChange(self):
        change = (self.hitpoint)/150 * 100
        change = int(change)

        if(change >= 20 and change <= 50):
            return Back.LIGHTMAGENTA_EX
        elif(change >= 0 and change <= 20):
            return Back.RED
        else: return Back.GREEN

    def isDestroyed(self):
        if(self.hitpoint<=0):
            return True
        else: 
            return False

    def attack(self,vil):
        if(self.isDestroyed()):
            for temp in vil.cannon:
                if(temp.row == self.row and temp.column == self.column):
                    vil.cannon.remove(temp)
                    vil.is_present[self.row][self.column] = 0
                    break
            return
        
        flag = 0
        for temp in vil.barbarian:
            x= temp.row
            y= temp.column
            if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= self.radius ):
                temp.hitpoint -= self.damage
                if(temp.hitpoint<=0):
                    vil.barbarian.remove(temp)
                    vil.is_present[x][y] = 0
                    flag = 1
                    break
                
        ok = 0
        if(flag==0):
            for temp in vil.archer:
                x= temp.row
                y= temp.column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= self.radius ):
                    temp.hitpoint -= self.damage
                    if(temp.hitpoint<=0):
                        vil.archer.remove(temp)
                        vil.is_present[x][y] = 0
                        ok = 1
                        break

        if(ok==0):
            if(len(vil.hero)>0):
                x = vil.hero[0].row
                y = vil.hero[0].column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= self.radius ):
                    vil.hero[0].health -= self.damage
                    if(vil.hero[0].health<=0):
                        vil.hero.remove(vil.hero[0])
                        vil.is_present[x][y] = 0
                    
