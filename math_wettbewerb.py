""" Mathematischer Wettbewerb, bei dem Sie Operationen in 30 Sekunden lösen müssen """


print("****************** MATH-WETTBEWERB ******************")
print("")
print(" Führen Sie so viele Operationen aus, wie Sie können")
print("             Sie haben 10 Sekunden Zeit")
print("")
print("******************************************************")
print("")
print("           Drücken Sie 'ENTER' zum Starten")

import random
import time

anfang = time.time()
zaehler = 0

while True:
    n1 = random.randint(1,9)
    n2 = random.randint(1,9)
    op1 = random.choice(["+", "*", "-", "/"])
    
    if op1 == "+":
        ergebnis = n1 + n2
        print(n1, op1 ,n2, end=" ")
    elif op1 == "*":
        ergebnis = n1 * n2
        print(n1, op1 ,n2, end=" ")
    elif op1 == "-":
        ergebnis = n1 - n2
        print(n1, op1 ,n2, end=" ")
    elif op1 == "/":
        ergebnis = n1 / n2
        print(n1, op1 ,n2, end=" ")
        
    antwort = float(input("= "))
    
    if antwort == ergebnis:
        print("BRAVO!! Punkt erreicht")
        zaehler += 1
    else:
        print("UPSS!!, fehlender Punkt\n")
        zaehler -= 1
    
    ende = time.time()    
    if ende - anfang >= 30:
        print("Die Zeit ist um\n")
        print("Verbracte Zeit: ",ende - anfang)
        print("VERDIENTE PUNKTE:", zaehler)
        break