from python_imagesearch.imagesearch import imagesearch, region_grabber, imagesearcharea
import pyautogui
from PIL import ImageGrab
from os import walk

for (dirpath, dirnames, i) in walk("./assets/"):
    filenames = i
    break

assets = ["./assets/div/windowslogo.png", "./assets/mystery.png", "./assets/div/map.png","./assets/1.png"]

class caseCoord:
  def __init__(self, name, x, y):
    self.name = name
    self.y = y
    self.x = x

def getCornerLeft():
    map = imagesearch(assets[1])
    if map[0] != -1:
        return map[0], map[1]
    else:
        return False, False

def oneClickLeft(loop):
    for i in range(loop):
        pyautogui.mouseDown(button="left")
        pyautogui.mouseUp(button="left")

def oneClickRight(loop):
    for i in range(loop):
        pyautogui.mouseDown(button="right")
        pyautogui.mouseUp(button="right")

def judgment(caseAround):
    countMine = 0
    dunno = []
    empty = 0
    countMystery = 0
    doSomething = False
    for i in caseAround:
        if i.name == "mystery":
            countMystery = countMystery + 1
            dunno.append(i)
        if i.name == "empty":
            empty = empty + 1
        elif i.name == "mine":
            countMine = countMine + 1
    if empty < 9 and countMystery < 9:
        if caseAround[4].name == str(len(dunno)+countMine):
            for i in dunno:
                pyautogui.moveTo(i.x, i.y)
                oneClickRight(1)
                doSomething = True
        elif caseAround[4].name == str(countMine):
            for i in dunno:
                pyautogui.moveTo(i.x, i.y)
                oneClickLeft(1)
                doSomething = True
    else:
        return False

    return doSomething

def fullScreen():
    windowsLogo = imagesearch(assets[0])
    if windowsLogo[0] != -1:
        pyautogui.click(x=windowsLogo[0], y=windowsLogo[1], clicks=1, button='left')
        pyautogui.keyDown('win')
        pyautogui.keyDown('up')
        pyautogui.keyUp('win')
        pyautogui.keyUp('up')
        return True
    else:
        return False

def clickOnMystery(x,y):
    if x == 0 and y == 0:
        mystery = imagesearch(assets[1])
        if mystery[0] != -1:
            pyautogui.moveTo(mystery[0], mystery[1])
            oneClickLeft(1)
    else:
        pyautogui.moveTo(x+205,y+140)
        oneClickLeft(1)

def scanAround(x,y):
    x = x-65-10
    y = y-65-10
    caseAround = []
    for l in range(9):        
        im = region_grabber((x, y, x+65, y+65))
        for i in filenames:
            case = imagesearcharea("./assets/"+i, x, y, x+65, y+65, 0.7, im)
            if case[0] != -1:
                caseAround.append(caseCoord(i.split(".")[0],x+case[0],y+case[1]))
                if i == "empty.png" or i != "outofmap.png" or i == "ah.png":
                    break
        x = x + 65
        if l == 2 or l == 5:
            y = y + 65
            x = x - 195
    return caseAround

def searchOne():
    oneCase = imagesearch(assets[3])
    if oneCase[0] != -1:
        return oneCase[0], oneCase[1] 
    else:
        return False

def extraScan(x,y):
    x = x-65-10-65
    y = y-65-10-65   
    isMystery = False
    for l in range(25):
        im = region_grabber((x, y, x+65, y+65))
        for i in filenames:
            case = imagesearcharea("./assets/"+i, x, y, x+65, y+65, 0.7, im)
            if case[0] != -1:
                if i == "mystery.png":
                    isMystery = True
                if i == "empty.png" or i != "outofmap.png" or i == "ah.png":
                        break
        x = x + 65
        if l == 4 or l == 9 or l == 14 or l == 19:
            x = x - 325
            y = y + 65
    return isMystery