import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from building import Huts,Wall,Townhall
from canon import Canon
from wizardTower import WizardTower

from datetime import datetime
now = datetime.now()
date_string = now.strftime("%H-%M-%S %d-%m-%Y")
file_string = "replay/"+date_string
fs = open(file_string,"w")

fs.write("-"*10)



class Village():
    def __init__(self,level):
        self.rows = 20
        self.columns = 50
        self.level = level
        self.is_present = [] # 0 for nothing is present , 1 for canon and 2 for townhall and 3 for huts,4 for wall,5 for wizard tower,6 for king
        self.initialisePresent()
        self.village = []
        self.initialiseVillage()
        self.huts = []
        self.initialiseHuts()
        self.walls = []
        self.print_walls()
        self.cannon = []
        self.initialiseCanon()
        self.wizardTower = []
        self.initialisewizardTower()
        self.townhall = []
        self.initialiseTownHall()
        self.spawnpoint = []
        self.spawnpoint.append([2,1])
        self.spawnpoint.append([2,20])
        self.spawnpoint.append([2,38])
        self.barbarian = []
        self.archer = []
        self.ballon = []
        # self.king = []
        # self.queen = []
        self.hero = []

       

    #done
    def show(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.is_present[i][j] == 0:
                    self.village[i][j] = Back.WHITE + " "

                elif self.is_present[i][j] == 1:
                    for temp in self.cannon:
                        if temp.row == i and temp.column == j:
                            self.village[i][j] = f"{Fore.BLACK}{temp.colorChange()}{Style.BRIGHT}C"
                            break
                            
                elif self.is_present[i][j] == 2:
                    self.village[i][j] = f"{Fore.BLACK}{self.townhall[0].colorChange()}{Style.BRIGHT}T"

                elif self.is_present[i][j] == 3:
                    for temp in self.huts:
                        if temp.row == i and temp.column == j:
                            self.village[i][j] = f"{Fore.BLACK}{temp.colorChange()}{Style.BRIGHT}H"
                            break

                elif self.is_present[i][j] == 4:
                    for temp in self.walls:
                        if temp.row == i and temp.column ==j:
                            self.village[i][j] =f"{Fore.BLACK}{temp.colorChange()}{Style.BRIGHT}W"
                            break

                elif self.is_present[i][j] == 5:
                    for temp in self.wizardTower:
                        if temp.row == i and temp.column ==j:
                            self.village[i][j] = f"{Fore.BLACK}{temp.colorChange()}{Style.BRIGHT}Z" # z for wizard tower
                            break
                
                elif self.is_present[i][j] == 6:
                    for temp in self.hero:
                        if temp.row == i and temp.column ==j:
                            self.village[i][j] = f"{Fore.BLACK}{Back.LIGHTBLUE_EX}{Style.BRIGHT}K"
                            break
                
                elif self.is_present[i][j] == 7:
                    for temp in self.hero:
                        if temp.row == i and temp.column ==j:
                            self.village[i][j] = f"{Fore.BLACK}{Back.LIGHTBLUE_EX}{Style.BRIGHT}Q"
                            break
                    

                for barbarian in self.barbarian:
                    self.village[barbarian.row][barbarian.column] = f"{Fore.BLACK}{barbarian.colorChange()}{Style.BRIGHT}B"

                for archer in self.archer:
                    self.village[archer.row][archer.column] = f"{Fore.BLACK}{archer.colorChange()}{Style.BRIGHT}A"
                
                for ballon in self.ballon:
                    self.village[ballon.row][ballon.column] = f"{Fore.BLACK}{ballon.colorChange()}{Style.BRIGHT}L" #l for loons
                
                print(self.village[i][j],end="")
                fs.write(self.village[i][j])
            print()
            fs.write("\n")

        fs.write("-"*10)
    
    #done
    def initialisePresent(self):
        for i in range(self.rows):
            temp_is_present = []
            for j in range(self.columns):
                val_is_present = 0
                temp_is_present.append(val_is_present)
            self.is_present.append(temp_is_present)
                

    #done
    def initialiseHuts(self):
        
        temphut1 = Huts(8, 14)
        temphut2 = Huts(6, 36)
        temphut3 = Huts(14, 14)
        temphut4 = Huts(14, 36)
        temphut5 = Huts(8, 36)
        self.huts.append(temphut1)
        self.huts.append(temphut2)
        self.huts.append(temphut3)
        self.huts.append(temphut4)
        self.huts.append(temphut5)
        self.village[temphut1.row][temphut1.column] = f"{Fore.BLACK}{temphut1.colorChange()}{Style.BRIGHT}H" 
        self.village[temphut2.row][temphut2.column] = f"{Fore.BLACK}{temphut2.colorChange()}{Style.BRIGHT}H" 
        self.village[temphut3.row][temphut3.column] = f"{Fore.BLACK}{temphut3.colorChange()}{Style.BRIGHT}H" 
        self.village[temphut4.row][temphut4.column] = f"{Fore.BLACK}{temphut4.colorChange()}{Style.BRIGHT}H" 
        self.village[temphut5.row][temphut5.column] = f"{Fore.BLACK}{temphut5.colorChange()}{Style.BRIGHT}H"
        self.is_present[temphut1.row][temphut1.column] = 3 
        self.is_present[temphut2.row][temphut2.column] = 3 
        self.is_present[temphut3.row][temphut3.column] = 3 
        self.is_present[temphut4.row][temphut4.column] = 3 
        self.is_present[temphut5.row][temphut5.column] = 3 
        
    #done
    def initialiseCanon(self):
        if(self.level == 0):
            tempcanon1 = Canon(6,18)
            tempcanon2 = Canon(14,32)
            self.cannon.append(tempcanon1)
            self.cannon.append(tempcanon2)
            self.village[tempcanon1.row][tempcanon1.column]= f"{Fore.BLACK}{tempcanon1.colorChange()}{Style.BRIGHT}C"
            self.village[tempcanon2.row][tempcanon2.column]= f"{Fore.BLACK}{tempcanon2.colorChange()}{Style.BRIGHT}C"
            self.is_present[tempcanon1.row][tempcanon1.column] = 1
            self.is_present[tempcanon2.row][tempcanon2.column] = 1 
        elif(self.level == 1):
            tempcanon1 = Canon(6,18)
            tempcanon2 = Canon(6,27)
            tempcanon3 = Canon(14,32)
            self.cannon.append(tempcanon1)
            self.cannon.append(tempcanon2)
            self.cannon.append(tempcanon3)
            self.village[tempcanon1.row][tempcanon1.column]= f"{Fore.BLACK}{tempcanon1.colorChange()}{Style.BRIGHT}C"
            self.village[tempcanon2.row][tempcanon2.column]= f"{Fore.BLACK}{tempcanon2.colorChange()}{Style.BRIGHT}C"
            self.village[tempcanon3.row][tempcanon3.column]= f"{Fore.BLACK}{tempcanon3.colorChange()}{Style.BRIGHT}C"
            self.is_present[tempcanon1.row][tempcanon1.column] = 1
            self.is_present[tempcanon2.row][tempcanon2.column] = 1
            self.is_present[tempcanon3.row][tempcanon3.column] = 1
        elif(self.level == 2):
            tempcanon1 = Canon(6,18)
            tempcanon2 = Canon(6,27)
            tempcanon3 = Canon(14,32)
            tempcanon4 = Canon(14,22)
            self.cannon.append(tempcanon1)
            self.cannon.append(tempcanon2)
            self.cannon.append(tempcanon3)
            self.cannon.append(tempcanon4)
            self.village[tempcanon1.row][tempcanon1.column]= f"{Fore.BLACK}{tempcanon1.colorChange()}{Style.BRIGHT}C"
            self.village[tempcanon2.row][tempcanon2.column]= f"{Fore.BLACK}{tempcanon2.colorChange()}{Style.BRIGHT}C"
            self.village[tempcanon3.row][tempcanon3.column]= f"{Fore.BLACK}{tempcanon3.colorChange()}{Style.BRIGHT}C"
            self.village[tempcanon4.row][tempcanon4.column]= f"{Fore.BLACK}{tempcanon4.colorChange()}{Style.BRIGHT}C"
            self.is_present[tempcanon1.row][tempcanon1.column] = 1
            self.is_present[tempcanon2.row][tempcanon2.column] = 1 
            self.is_present[tempcanon3.row][tempcanon3.column] = 1
            self.is_present[tempcanon4.row][tempcanon4.column] = 1

     #done
    def initialisewizardTower(self):
        if(self.level == 0):
            tempWizardTower1 = WizardTower(10, 18)
            tempWizardTower2 = WizardTower(10, 32)
            self.wizardTower.append(tempWizardTower1)
            self.wizardTower.append(tempWizardTower2)
            self.village[tempWizardTower1.row][tempWizardTower1.column]= f"{Fore.BLACK}{tempWizardTower1.colorChange()}{Style.BRIGHT}Z"
            self.village[tempWizardTower2.row][tempWizardTower2.column]= f"{Fore.BLACK}{tempWizardTower2.colorChange()}{Style.BRIGHT}Z"
            self.is_present[tempWizardTower1.row][tempWizardTower1.column] = 5
            self.is_present[tempWizardTower2.row][tempWizardTower2.column] = 5 
        elif(self.level == 1):
            tempWizardTower1 = WizardTower(10, 18)
            tempWizardTower2 = WizardTower(10, 32)
            tempWizardTower3 = WizardTower(9, 25)
            self.wizardTower.append(tempWizardTower1)
            self.wizardTower.append(tempWizardTower2)
            self.wizardTower.append(tempWizardTower3)
            self.village[tempWizardTower1.row][tempWizardTower1.column]= f"{Fore.BLACK}{tempWizardTower1.colorChange()}{Style.BRIGHT}Z"
            self.village[tempWizardTower2.row][tempWizardTower2.column]= f"{Fore.BLACK}{tempWizardTower2.colorChange()}{Style.BRIGHT}Z"
            self.village[tempWizardTower3.row][tempWizardTower3.column]= f"{Fore.BLACK}{tempWizardTower3.colorChange()}{Style.BRIGHT}Z"
            self.is_present[tempWizardTower1.row][tempWizardTower1.column] = 5
            self.is_present[tempWizardTower2.row][tempWizardTower2.column] = 5
            self.is_present[tempWizardTower3.row][tempWizardTower3.column] = 5
        elif(self.level == 2):
            tempWizardTower1 = WizardTower(10, 18)
            tempWizardTower2 = WizardTower(10, 32)
            tempWizardTower3 = WizardTower(9, 25)
            tempWizardTower4 = WizardTower(16, 25)
            self.wizardTower.append(tempWizardTower1)
            self.wizardTower.append(tempWizardTower2)
            self.wizardTower.append(tempWizardTower3)
            self.wizardTower.append(tempWizardTower4)
            self.village[tempWizardTower1.row][tempWizardTower1.column]= f"{Fore.BLACK}{tempWizardTower1.colorChange()}{Style.BRIGHT}Z"
            self.village[tempWizardTower2.row][tempWizardTower2.column]= f"{Fore.BLACK}{tempWizardTower2.colorChange()}{Style.BRIGHT}Z"
            self.village[tempWizardTower3.row][tempWizardTower3.column]= f"{Fore.BLACK}{tempWizardTower3.colorChange()}{Style.BRIGHT}Z"
            self.village[tempWizardTower4.row][tempWizardTower4.column]= f"{Fore.BLACK}{tempWizardTower4.colorChange()}{Style.BRIGHT}Z"
            self.is_present[tempWizardTower1.row][tempWizardTower1.column] = 5
            self.is_present[tempWizardTower2.row][tempWizardTower2.column] = 5
            self.is_present[tempWizardTower3.row][tempWizardTower3.column] = 5
            self.is_present[tempWizardTower4.row][tempWizardTower4.column] = 5

    #done
    def initialiseVillage(self):
        for i in range(self.rows):
            temp = []
            for j in range(self.columns):
                val = Back.WHITE + " "
                temp.append(val) 
            self.village.append(temp)
            
    
    #done
    def initialiseTownHall(self):
        th = Townhall(10,24)
        self.townhall.append(th)

        for i in range(4):
            for j in range(3):
                self.village[th.topleft+i][th.topright+j] = f"{Fore.BLACK}{th.colorChange()}{Style.BRIGHT}T"
                self.is_present[th.topleft+i][th.topright+j] = 2
        


    #done 
    def print_walls(self):
        for j in range(6,43):
            wall = Wall(4,j)
            wall2 = Wall(17,j)
            self.village[wall.row][wall.column] = f"{Back.YELLOW}{Style.BRIGHT} "
            self.village[wall2.row][wall2.column] = f"{Back.YELLOW}{Style.BRIGHT} "
            self.walls.append(wall)
            self.walls.append(wall2)
            self.is_present[wall.row][wall.column] = 4
            self.is_present[wall.row][wall.column] = 4
            self.is_present[wall2.row][wall2.column] = 4
            self.is_present[wall2.row][wall2.column] = 4

        for i in range(4,17):
            wall = Wall(i,6)
            wall2 = Wall(i,42)
            self.village[wall.row][wall.column] = f"{Back.YELLOW}{Style.BRIGHT} "
            self.village[wall2.row][wall2.column] = f"{Back.YELLOW}{Style.BRIGHT} "
            self.walls.append(wall)
            self.walls.append(wall2)
            self.is_present[wall.row][wall.column] = 4
            self.is_present[wall.row][wall.column] = 4
            self.is_present[wall2.row][wall2.column] = 4
            self.is_present[wall2.row][wall2.column] = 4



        
