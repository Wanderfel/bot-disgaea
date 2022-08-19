import os
import numpy as np
import pprint

def findMonsterSpritePack(monsterList):
    dictList = returnMonstersDict(monsterList)
    dictionaryList = {}

    for dict in dictList:
       
        filesList = returnImageFilesByPath(f"assets/combat/monsters/{dict}/")
        dictionaryList[dict] = []
        
        for file in filesList:
           dictionaryList[dict].append(f"assets/combat/{dict}/{file}")
        
    
    return dictionaryList

def returnImageFilesByPath(path):
    filesList = []
    for (root, dirs, file) in os.walk(path):
        for f in file:
            filesList.append(f)
    return filesList

def returnMonstersDict(monsterList):
    allMonsters =  os.listdir("assets/combat/monsters")
    filteredList = np.intersect1d(np.array(monsterList),np.array(allMonsters))
    return filteredList
    

monsterDictionary = findMonsterSpritePack(["pizzicato","redskull"])
pprint.pprint(monsterDictionary)

