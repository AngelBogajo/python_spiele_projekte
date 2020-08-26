""" Spiel Schnick, Schnack, Schnuck """

import random


optionen = ["Papier", "Stein","Schere"]

pc = random.choice(optionen)

spielen = True

while spielen:
    spieler = input("Geben Sie eine Option ein: ")
    if spieler == "Stein":
        if pc == "Stein":
            print("PC wählt auch Stein. UNENTSCHIEDEN")
        elif pc == "Schere":
            print("Stein zerbricht Schere – Stein siegt. DU GEWINNST")
        else:
            print("Papier umwickelt Stein – Papier siegt. PC GEWINNT")
    if spieler == "Papier":
        if pc == "Papier":
            print("PC wählt auch Papier. UNENTSCHIEDEN")
        elif pc == "Schere":
            print("Schere schneidet Papier – die Schere siegt. PC GEWINNT")
        else:
            print("Papier umwickelt Stein – Papier siegt. DU GEWINNST")
    if spieler == "Schere":
        if pc == "Schere":
            print("PC wählt auch Schere. UNENTSCHIEDEN")
        elif pc == "Papier":
            print("Schere schneidet Papier – die Schere siegt. DU GEWINNST")
        else:
            print("Stein zerbricht Schere – Stein siegt. PC GEWINNT")