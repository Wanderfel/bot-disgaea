import pyautogui as pg
import pydirectinput as pd
import time
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def clickLeftByPrint(imagePath, confidence = 0.95, speed = 1, chronos = 0.5):
    sn = pg.locateOnScreen(imagePath, confidence = confidence)
    if sn:
        print(f'Encontrado! {imagePath}')
        width = sn.width
        height = sn.height
        leftPos = sn.left + (width/2)
        topPos = sn.top + (height/2)
        pg.moveTo(leftPos, topPos, speed)
        pg.mouseDown(button='left') 
        pg.mouseUp(button='left')
        time.sleep(chronos)
        return sn
    return sn

def pressKey(key, chronos = 0):
    pd.press(key)
    time.sleep(chronos)

def skipNadiaDialog():
    repeatSequence("k",2)
    time.sleep(2)
    print(f"Skipou diálogo da Nadia")

def goToSequence(sequenceList, intervalTime = 1, chronos = 0):
    for move in sequenceList:
        pressKey(move)
        time.sleep(intervalTime)
    time.sleep(chronos)

def repeatSequence(command,howMuch):
    listSequence = [command] * howMuch
    goToSequence(listSequence, intervalTime = 1)
    time.sleep(1)

def selectElement(imagePath, chronos = 0.5):
    clickLeftByPrint(imagePath, confidence = 0.80, speed = 0.5, chronos = chronos)

def attack():
    goToSequence(["k","s","k","k"])
    print("Atacou") 

def endTurn():
    goToSequence(["i","s","k"]) 
    print("Finalizou o Turno")

def endAttack():
    attack()
    endTurn()

def move():
    goToSequence(["k","k"])
    print("Selecionou a opção Move")

def rotateCamera(direction, howMuch):
    repeatSequence(direction,howMuch)


def plainairName():
    goToSequence(["k","k","k"])
    print("Selecionou a Plainair")

def changeMouseControls():
    imagePath = "assets/area-select/mouse-select.png"
    goToSequence(["i","w","k"], intervalTime = 0.5)
    clickLeftByPrint(imagePath, confidence = 0.95, speed = 1, chronos = 0.5)
    goToSequence(["esc","esc"])
    print("Desabilitou o mouse")
 




        

    
        