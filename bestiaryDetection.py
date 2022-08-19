import actionController as ac
import pyautogui as pg
import time
import searchSprite as sp

def onlyDetect(imagePath, confidence = 0.95, chronos = 0.5):
    sn = pg.locateOnScreen(imagePath, confidence = confidence)
 
    if sn:
        print(f'Encontrado! {imagePath}')
        time.sleep(chronos)
        return sn
    return sn


def detectPizzicato():
    sprites = sp.findMonsterSpritePack(["pizzicato"])
    listPathPizzicato = sprites["pizzicato"]
    for path in listPathPizzicato:
        if (onlyDetect(path, confidence = 0.80)):
            return True
    return False


def detectHobbit(): 
    sprites = sp.findMonsterSpritePack(["hobbit"])
    listPathHobbit = sprites["hobbit"]
    for path in listPathHobbit:
        if (onlyDetect(path, confidence = 0.80)):
            return True
    return False

def detectRedskull():
    sprites = sp.findMonsterSpritePack(["redskull"])
    listPathRedskull = sprites["redskull"]
    for path in listPathRedskull:      
        if (onlyDetect(path, confidence = 0.80)):
            return True
    return False




