
import actionController as cc
import bestiaryDetection as bd
import time
import winsound

engageEnemy = ["w","w","w","w","w","k"]
goToRightPizzicato = ["d","d","d","w","w","k"]
goToLeftPizzicato = ["a", "a", "a", "s", "a", "a", "w","k"]
skipBountyPreview = ["k","k"]
listMonsters = ["pizzicato","redskull","hobbit"]


print("Inicio da sessão")
time.sleep(5)
winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

while True:
    cc.pressKey("k",chronos = 0.5)
    time.sleep(5)
    print("Entrou no combate...")
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    cc.plainairName();
    cc.goToSequence(engageEnemy, intervalTime=0.5);
    time.sleep(3)
    cc.endAttack()
    time.sleep(13)  
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

    print("PRIMEIRA INVESTIDA")
    pizzicatoDetected = bd.detectPizzicato()
    while pizzicatoDetected:
        cc.endAttack()
        time.sleep(10)
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        pizzicatoDetected = bd.detectPizzicato()
        print(pizzicatoDetected)

    cc.move()
    time.sleep(0.5)
    cc.goToSequence(engageEnemy, intervalTime=0.5)
    time.sleep(3)
    cc.rotateCamera("e", 2)
    time.sleep(3)
    cc.endAttack()
    time.sleep(15)
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    print("SEGUNDA INVESTIDA")
    pizzicatoDetected = bd.detectPizzicato()
    hobbitDetected = bd.detectHobbit()
    while (pizzicatoDetected or hobbitDetected):
        cc.endAttack()
        time.sleep(15)
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        pizzicatoDetected = bd.detectPizzicato()
        hobbitDetected = bd.detectHobbit()
        print(pizzicatoDetected)
        print(hobbitDetected)

    time.sleep(10)
    cc.move()
    cc.goToSequence(goToRightPizzicato, intervalTime=0.5);
    time.sleep(4)
    cc.endAttack()
    time.sleep(2)
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    cc.move()
    cc.goToSequence(goToLeftPizzicato)
    time.sleep(4)
    cc.endAttack()
    time.sleep(3)
    cc.pressKey(skipBountyPreview)
    time.sleep(4)






















