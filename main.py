import os
import sys
from threading import Timer

sys.path.append('./src')

from village import Village
from building import *
from canon import Canon
from king import King
from queen import Queen
from game_input import *
from barbarian import Barbarian
from ballon import Ballon
from archer import Archer
import time

starttime = time.time()
lastUpdate = starttime

ask = input("Press 1 to choose king and press 2 to choose queen: ")
ask = int(ask)

getch = Get()

troop_limit = [6,6,6] # [archer,ballon,barbarian]

cnt = 0
vil = Village(cnt)
if(ask == 1):
    king = King(15,2)
    vil.hero.append(king)
    vil.is_present[15][2] = 6 
else:
    queen = Queen(15,2)
    vil.hero.append(queen)
    vil.is_present[15][2] = 7  
    

vil.show()
if(ask == 1):
    print("King's Health\n")
    vil.hero[0].healthBar()
else:
    print("Queen's Health\n")
    vil.hero[0].healthBar()
print()

if(ask==1):
    while True:
        ch = input_to(getch)
    
        if(ch == 'q'):
            break
        if(ch == 'w' or ch=='a' or ch=='s' or ch=='d'):
            if(len(vil.hero)>0):
                vil.hero[0].move(ch,vil)
        if(ch == ' '):
            if(len(vil.hero)>0):
                vil.hero[0].attack(ch,vil)
        
        
        # spawn barbarian
        if(ch == 'y' or ch=='u' or ch=='i'):
            if(troop_limit[2]>0):
                if(ch == 'y'):
                    vil.barbarian.append(Barbarian(vil.spawnpoint[0][0], vil.spawnpoint[0][1]))
                elif(ch=='u'):
                    vil.barbarian.append(Barbarian(vil.spawnpoint[1][0], vil.spawnpoint[1][1]))
                elif(ch == 'i'):
                    vil.barbarian.append(Barbarian(vil.spawnpoint[2][0], vil.spawnpoint[2][1]))

            troop_limit[2] -= 1
        
        # spawn archer
        if(ch == 'k' or ch=='j' or ch=='l'):
            if(troop_limit[0]>0):
                if(ch == 'j'):
                    vil.archer.append(Archer(vil.spawnpoint[0][0], vil.spawnpoint[0][1]))
                elif(ch=='k'):
                    vil.archer.append(Archer(vil.spawnpoint[1][0], vil.spawnpoint[1][1]))
                elif(ch == 'l'):
                    vil.archer.append(Archer(vil.spawnpoint[2][0], vil.spawnpoint[2][1]))

            troop_limit[0] -= 1

        # spawn ballon
        if(ch == 'n' or ch=='b' or ch=='m'):
            if(troop_limit[1]>0):
                if(ch == 'b'):
                    vil.ballon.append(Ballon(vil.spawnpoint[0][0], vil.spawnpoint[0][1]))
                elif(ch=='n'):
                    vil.ballon.append(Ballon(vil.spawnpoint[1][0], vil.spawnpoint[1][1]))
                elif(ch == 'm'):
                    vil.ballon.append(Ballon(vil.spawnpoint[2][0], vil.spawnpoint[2][1]))

            troop_limit[1] -= 1

        if(ch == 'r'):
            arr = []
            for i in vil.barbarian:
                arr.append(i)
            for i in vil.archer:
                arr.append(i)
            for i in vil.ballon:
                arr.append(i)
            if(len(vil.hero)>0):
                arr.append(vil.hero[0])
            for i in arr:
                i.rageSpell()
                
        if(ch == 'h'):
            arr = []
            for i in vil.barbarian:
                arr.append(i)
            for i in vil.archer:
                arr.append(i)
            for i in vil.ballon:
                arr.append(i)
            if(len(vil.hero)>0):
                arr.append(vil.hero[0])
            for i in arr:
                i.healSpell()
        

        os.system('clear')
        if(time.time()-lastUpdate>1):
            for i in vil.barbarian:
                i.move(vil)

            for i in vil.archer:
                i.move(vil)

            for i in vil.ballon:
                i.move(vil)

            for i in vil.cannon:
                i.attack(vil)

            for i in vil.wizardTower:
                i.attack(vil)
            
            lastUpdate = time.time()

        if(len(vil.huts)==0 and len(vil.cannon)==0 and len(vil.townhall)==0 and len(vil.wizardTower)==0):
            cnt+=1
            # print("Level is",vil.level+1)
            temp = Village(cnt)
            troop_limit = [6,6,6]
            vil = temp
            if(ask == 1):
                king = King(15,2)
                vil.hero.append(king)
                vil.is_present[15][2] = 6 
            else:
                queen = Queen(15,2)
                vil.hero.append(queen)
                vil.is_present[15][2] = 7 
            if(cnt==3):
                print("Game over - Win")
                break
            vil.level = cnt
            
        # elif(vil.hero[0].isDead() and len(vil.barbarian)==0):
        #     print("Game over - Defeat")
        #     break
        elif(len(vil.hero)==0 and len(vil.barbarian)==0 and len(vil.archer)==0 and len(vil.ballon)==0):
            print("Game over - Defeat")
            break
            
        vil.show()
        if(len(vil.hero)>0):
            print("King's Health\n")
            vil.hero[0].healthBar()

        # if(vil.level==3):
        #     print("Game Over  - Win")
        #     break
        # print(cnt)
        print()


elif(ask==2):
    while True:
        ch = input_to(getch)
    
        if(ch == 'q'):
            break
        if(ch == 'w' or ch=='a' or ch=='s' or ch=='d'):
            if(len(vil.hero)>0):
                vil.hero[0].move(ch,vil)
        if(ch == ' '):
            if(len(vil.hero)>0):
                vil.hero[0].attack(ch,vil)
        if(ch == 'p'):
            if(len(vil.hero)>0):
                r = Timer(5.0, vil.hero[0].specialAttack, [ch,vil])
                r.start()
        # spawn barbarian
        if(ch == 'y' or ch=='u' or ch=='i'):
            if(troop_limit[2]>0):
                if(ch == 'y'):
                    vil.barbarian.append(Barbarian(vil.spawnpoint[0][0], vil.spawnpoint[0][1]))
                elif(ch=='u'):
                    vil.barbarian.append(Barbarian(vil.spawnpoint[1][0], vil.spawnpoint[1][1]))
                elif(ch == 'i'):
                    vil.barbarian.append(Barbarian(vil.spawnpoint[2][0], vil.spawnpoint[2][1]))

            troop_limit[2] -= 1
        
        # spawn archer
        if(ch == 'k' or ch=='j' or ch=='l'):
            if(troop_limit[0]>0):
                if(ch == 'j'):
                    vil.archer.append(Archer(vil.spawnpoint[0][0], vil.spawnpoint[0][1]))
                elif(ch=='k'):
                    vil.archer.append(Archer(vil.spawnpoint[1][0], vil.spawnpoint[1][1]))
                elif(ch == 'l'):
                    vil.archer.append(Archer(vil.spawnpoint[2][0], vil.spawnpoint[2][1]))

            troop_limit[0] -= 1

        # spawn ballon
        if(ch == 'n' or ch=='b' or ch=='m'):
            if(troop_limit[1]>0):
                if(ch == 'b'):
                    vil.ballon.append(Ballon(vil.spawnpoint[0][0], vil.spawnpoint[0][1]))
                elif(ch=='n'):
                    vil.ballon.append(Ballon(vil.spawnpoint[1][0], vil.spawnpoint[1][1]))
                elif(ch == 'm'):
                    vil.ballon.append(Ballon(vil.spawnpoint[2][0], vil.spawnpoint[2][1]))

            troop_limit[1] -= 1

        if(ch == 'r'):
            arr = []
            for i in vil.barbarian:
                arr.append(i)
            for i in vil.archer:
                arr.append(i)
            for i in vil.ballon:
                arr.append(i)
            if(len(vil.hero)>0):
                arr.append(vil.hero[0])
            for i in arr:
                i.rageSpell()
                
        if(ch == 'h'):
            arr = []
            for i in vil.barbarian:
                arr.append(i)
            for i in vil.archer:
                arr.append(i)
            for i in vil.ballon:
                arr.append(i)
            if(len(vil.hero)>0):
                arr.append(vil.hero[0])
            for i in arr:
                i.healSpell()

        os.system('clear')
        if(time.time()-lastUpdate>1):
            for i in vil.barbarian:
                i.move(vil)

            for i in vil.archer:
                i.move(vil)

            for i in vil.ballon:
                i.move(vil)

            for i in vil.cannon:
                i.attack(vil)

            for i in vil.wizardTower:
                i.attack(vil)
            
            lastUpdate = time.time()

        if(len(vil.huts)==0 and len(vil.cannon)==0 and len(vil.townhall)==0 and len(vil.wizardTower)==0):
            cnt+=1
            # print("Level is",vil.level+1)
            temp = Village(cnt)
            troop_limit = [6,6,6]
            vil = temp
            if(ask == 1):
                king = King(15,2)
                vil.hero.append(king)
                vil.is_present[15][2] = 6 
            else:
                queen = Queen(15,2)
                vil.hero.append(queen)
                vil.is_present[15][2] = 7 
            if(cnt==3):
                print("Game over - Win")
                break
            vil.level = cnt
            
            
        # elif(vil.king[0].isDead() and len(vil.barbarian)==0):
        #     print("Game over - Defeat")
        #     break
        elif(len(vil.hero)==0 and len(vil.barbarian)==0 and len(vil.archer)==0 and len(vil.ballon)==0):
            print("Game over - Defeat")
            break
        vil.show()
        if(len(vil.hero)>0):
            print("Queen's Health\n")
            vil.hero[0].healthBar()
        # print(cnt,vil.level)
        # if(vil.level==3):
        #     print("Game Over  - Win")
        #     break
        print()







