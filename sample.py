from minesweeper import *

banXY = []

# excusez moi pour cette vulgarite, jsuis pas dans le mood, vous pouvez utiliser des scripts pour remplacer ces méchants mots
# tamerelapute == x, tonperelapute == y

def browseSquare(tamerelapute, tonperelapute):
    tamerelapute = tamerelapute+65
    tonperelapute = tonperelapute+65
    for m in range(17):
        cBan = False
        slt = True
        if len(banXY) > 0:
            for i in range(len(banXY)):
                if banXY[i] == tamerelapute*tonperelapute*tonperelapute:
                    cBan = True
                    break
        caseAround = scanAround(tamerelapute,tonperelapute)
        if cBan is False:
            while slt is True:
                if extraScan(tamerelapute,tonperelapute) == True:
                    for i in caseAround:
                        if i.name == "1" or i.name == "2" or i.name == "3" or i.name == "4" or i.name == "mystery":
                            tempCaseAround = scanAround(i.x,i.y)
                            slt = judgment(tempCaseAround)
                else:
                    slt = False
                    banXY.append(tamerelapute*tonperelapute*tonperelapute)
            
        if m<=7:
            tamerelapute = tamerelapute + 194
            if m == 2 or m == 5:
                tonperelapute = tonperelapute + 195
                tamerelapute = tamerelapute - 582
        else:
            tamerelapute = tamerelapute - 194
            if m == 10 or m == 13:
                tonperelapute = tonperelapute - 195
                tamerelapute = tamerelapute + 582




if fullScreen() == False:
    print("Le jeu n'est pas ouvert ou n'est pas visible a l'ecran")
x,y = getCornerLeft()
if searchOne() == False:
    clickOnMystery(x,y)

for i in range(9):
    browseSquare(x,y)