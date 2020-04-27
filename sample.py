from minesweeper import *
import pyautogui

if fullScreen() == False:
    print("Le jeu n'est pas ouvert ou n'est pas visible a l'ecran")
x,y = getCornerLeft()
if searchOne() == False:
    clickOnMystery(x,y)

for i in range(9):
    x = x+65
    y = y+65
    cBan = False
    for m in range(17):
        slt = True
        if len(banXY) > 0:
            for i in range(len(banXY)):
                if banXY[i] == x*y*y:
                    cBan = True
                    break
        # if cBan is False:
        # while slt is True:
        caseAround = scanAround(x,y)
        pyautogui.moveTo(x,y)
        if extraScan(x,y) == True:
            for i in caseAround:
                if i.name == "1" or i.name == "2" or i.name == "3" or i.name == "4":
                    tempCaseAround = scanAround(i.x,i.y)
                    slt = judgment(tempCaseAround)
                # else:
                #     slt = False
                #     banXY.append(x*y*y)
            
        if m<=7:
            x = x + 194
            if m == 2 or m == 5:
                y = y + 195
                x = x - 582
        else:
            x = x - 194
            if m == 10 or m == 13:
                y = y - 195
                x = x + 582