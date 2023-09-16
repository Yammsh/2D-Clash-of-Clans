from village import *
from canon import Canon
from building import *
import math
vil = Village(0)

class King():
    def __init__(self,row,column):
        self.row=row
        self.column=column
        self.damage = 20
        self.health = 150
        self.initial_health = 150
        self.speed = 1
        self.attack_radius = 4 # radius in which the king attacks around him

    def isDead(self):
        if(self.health<=0):
            return True
        else: 
            return False

    def move(self,ch,vil):
        if(self.health > 0):
            flag = False # Flag to indicate if the king can move at the desired position or not

            
            if(ch=='w'):
                temp_row = max(0,self.row-self.speed)
                for row in range(self.row-1,max(0,self.row-self.speed-1),-1):
                    if(vil.is_present[row][self.column]!=0):
                        temp_row = max(0,row+1)
                        flag = True
                        break
                if(vil.is_present[temp_row][self.column]==0):
                    vil.is_present[self.row][self.column] = 0
                    self.row = temp_row
                    flag = True
            
            elif(ch=='s'):
                temp_row = min(vil.rows-1,self.row+self.speed)
                for row in range(self.row+1,min(vil.rows-1,self.row+self.speed+1),1):
                    if(vil.is_present[row][self.column]!=0):
                        temp_row = min(vil.rows-1,row-1)
                        flag = True
                        break
                if(vil.is_present[temp_row][self.column]==0 ):
                    vil.is_present[self.row][self.column] = 0
                    self.row = temp_row
                    flag = True

            elif(ch=='a'):
                temp_column = max(0,self.column-self.speed)
                for column in range(self.column-1,max(0,self.column-self.speed-1),-1):
                    if(vil.is_present[self.row][column]!=0):
                        temp_column = max(0,column+1)
                        flag = True
                        break
                if(vil.is_present[self.row][temp_column]==0 ):
                    vil.is_present[self.row][self.column] = 0
                    self.column = temp_column
                    flag = True
            
            elif(ch=='d'):
                temp_column = min(vil.columns-1,self.column+self.speed)
                for column in range(self.column+1,min(vil.columns-1,self.column+self.speed+1),1):
                    if(vil.is_present[self.row][column]!=0):
                        temp_column = min(vil.columns-1,column-1)
                        flag = True
                        break

                if(vil.is_present[self.row][temp_column]==0 ):
                    vil.is_present[self.row][self.column] = 0
                    self.column = temp_column
                    flag = True
            
            if(flag):
                vil.is_present[self.row][self.column] = 6

    def attack(self,ch,vil):
        if(self.health>0):
            # for huts
            for temp in (vil.huts):
                x = temp.row
                y = temp.column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= self.attack_radius ):
                    temp.hitpoint -= self.damage
                    # vil.is_present[temp.row][temp.column] = 3
                    if(temp.isDestroyed()):
                        vil.huts.remove(temp)
                        vil.is_present[x][y] = 0
            
            # for canon
            for temp in (vil.cannon):
                x = temp.row
                y = temp.column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= self.attack_radius ):
                    temp.hitpoint -= self.damage
                    # vil.is_present[temp.row][temp.column] = 1
                    if(temp.isDestroyed()):
                        vil.cannon.remove(temp)
                        vil.is_present[x][y] = 0

            # for wizard Tower
            for temp in (vil.wizardTower):
                x = temp.row
                y = temp.column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= self.attack_radius ):
                    temp.hitpoint -= self.damage
                    # vil.is_present[temp.row][temp.column] = 2
                    if(temp.isDestroyed()):
                        vil.wizardTower.remove(temp)
                        vil.is_present[x][y] = 0

            # for townhall
            if(len(vil.townhall)>0):
                temp_th = vil.townhall[0]
                for i in range(4):
                    flag = 0
                    for j in range(3):
                        if( math.sqrt((temp_th.topleft-self.row+i)**2 + (temp_th.topright-self.column+j)**2) <= self.attack_radius ):
                            temp_th.hitpoint -= self.damage
                            # for k in range(4):
                            #     for l in range(3):
                            #         vil.is_present[temp_th.topleft+k][temp_th.topright+l] = 2
                            if(temp_th.isDestroyed()):
                                for m in range(4):
                                    for n in range(3):
                                        vil.is_present[temp_th.topleft+m][temp_th.topright+n] = 0
                                vil.townhall.clear()

                            flag=1
                            break
                    if(flag): break
            
            # for wall
            for temp in (vil.walls):
                x = temp.row
                y = temp.column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= self.attack_radius ):
                    temp.hitpoint -= self.damage
                    # vil.is_present[temp.row][temp.column] = 4
                    if(temp.isDestroyed()):
                        vil.walls.remove(temp)
                        vil.is_present[x][y] = 0
            
    def specialAttack(self,ch,vil):
        pass
            
    def healthBar(self):
        if(self.health>0):
            change = (self.health)/(150) * 100
            change = change//1
            for i in range(int(change)):
                print(f"{Back.RED}{Style.BRIGHT} ",end="")

    def rageSpell(self):
        if(self.health>0):
            self.damage *= 2
            self.speed *= 2

    def healSpell(self):
        if(self.health>0):
            self.health = min(self.health*(1.5),self.initial_health)


            
               




        
