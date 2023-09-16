from village import *
import math

class WizardTower():
    def __init__(self,row,column):
        self.damage = 20
        self.row=row
        self.column=column
        self.hitpoint = 30
        self.radius = 4

    def otherAttack(self,vil,wiz_x,wiz_y):

        # for barbarian
        for temp in vil.barbarian:
            x= temp.row
            y= temp.column
            if( math.sqrt((x-wiz_x)**2 + (y-wiz_y)**2) <= 3 ):
                temp.hitpoint -= self.damage
                if(temp.hitpoint<=0):
                    vil.barbarian.remove(temp)
                    vil.is_present[x][y] = 0

        # for archer
        for temp in vil.archer:
            x= temp.row
            y= temp.column
            if( math.sqrt((x-wiz_x)**2 + (y-wiz_y)**2) <= 3 ):
                temp.hitpoint -= self.damage
                if(temp.hitpoint<=0):
                    vil.archer.remove(temp)
                    vil.is_present[x][y] = 0
        
                
        # for king
        if(len(vil.hero)>0):
            x = vil.hero[0].row
            y = vil.hero[0].column
            if( math.sqrt((x-wiz_x)**2 + (y-wiz_y)**2) <= 3 ):
                vil.hero[0].health -= self.damage
                if(vil.hero[0].health<=0):
                    vil.hero.remove(vil.hero[0])
                    vil.is_present[x][y] = 0

        
        # for ballon
        for temp in vil.ballon:
            x= temp.row
            y= temp.column
            if( math.sqrt((x-wiz_x)**2 + (y-wiz_y)**2) <= 3 ):
                temp.hitpoint -= self.damage
                if(temp.hitpoint<=0):
                    vil.ballon.remove(temp)
                    vil.is_present[x][y] = 0
        
        return


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
            for temp in vil.wizardTower:
                if(temp.row == self.row and temp.column == self.column):
                    vil.wizardTower.remove(temp)
                    vil.is_present[self.row][self.column] = 0
                    break
            return
        
        flag = 0
        for temp in vil.barbarian:
            x= temp.row
            y= temp.column
            if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= self.radius ):
                # temp.hitpoint -= self.damage
                self.otherAttack(vil,x,y)
                # if(len(vil.barbarian)>0 and temp.hitpoint<=0):
                #     vil.barbarian.remove(temp)
                #     vil.is_present[x][y] = 0
                flag = 1
                break
                
        ok = 0
        if(flag==0):
            for temp in vil.archer:
                x= temp.row
                y= temp.column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= self.radius ):
                    # temp.hitpoint -= self.damage
                    self.otherAttack(vil,x,y)
                    # if(len(vil.archer)>0 and temp.hitpoint<=0):
                    #     vil.archer.remove(temp)
                    #     vil.is_present[x][y] = 0
                    ok = 1
                    break

        ballonflag = 0                
        if(ok==0):
            if(len(vil.hero)>0):
                x = vil.hero[0].row
                y = vil.hero[0].column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= self.radius ):
                    vil.hero[0].health -= self.damage
                    self.otherAttack(vil,x,y)
                    # if(king.health<=0 and len(vil.hero)>0):
                    #     vil.is_present[king.row][king.column] = 0
                    #     vil.hero.remove(temp)
                    ballonflag = 1

        if(ballonflag==0):
            for temp in vil.ballon:
                x= temp.row
                y= temp.column
                if( math.sqrt((x-self.row)**2 + (y-self.column)**2) <= self.radius ):
                    # temp.hitpoint -= self.damage
                    self.otherAttack(vil,x,y)
                    # if(temp.hitpoint<=0 and len(vil.ballon)>0):
                    #     vil.ballon.remove(temp)
                    #     vil.is_present[x][y] = 0
                    break

                    
