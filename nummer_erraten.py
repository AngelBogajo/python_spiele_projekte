""" Spiel, das eine Zufallszahl zwischen 1 und 100 generiert, die erraten werden muss.
Bei jedem Versuch wird angezeigt, ob die von Ihnen eingegebene Zahl größer oder kleiner 
als die Geheimzahl ist.
Sie haben nur 7 Versuche, nach 7 Versuchen endet das Programm und zeigt an, dass Sie 
ausgeschieden sind. Wenn Sie die Geheimzahl richtig erraten haben, zeigt dies an, dass
Sie sie erraten haben, und das Spiel ist beendet. """

print("**** ERRATEN SIE DIE GEHEIMZAHL! ****")
import random

zahl_zu_erraten = random.randint(1,100)    # Zufallszahl zwischen 1 und 100.

optionen_hoch = ["Uff!!, soll kleine sein.","zu hoch.", "wir suchen eine kleinere Nummer.",
                  "weiter runter."]

optionen_niedrige = ["Wir suchen eine größere Nummer.","zu niedrig.","Uff!! soll größer Nummer sein.",
                  "weiter hoch."]

zaehler = 0                         
spielen = True

while spielen:
    rate = int(input("\nGeben Sie eine Zahl zwischen 1 und 100 ein: "))
    
    hoch = random.choice(optionen_hoch)         # bei jedem Versuch wird eine Option aus der Liste ausgewählt
    niedrig = random.choice(optionen_niedrige)  # bei jedem Versuch wird eine Option aus der Liste ausgewählt
    
    if zahl_zu_erraten == rate:
        print("\nWoow!! Respekt!!, Sie haben es geschafft.")
        spielen = False
    elif zaehler == 6:
        print("\nSie haben Ihre letzte Patrone verbrannt. Sie sind raus!.")
        print("\nDie richtige Nummer war: ",zahl_zu_erraten,"\n")       # Geheimzahl zeigen
        zaehler = 0                                                     # Reset zaehler
        weiter = ""
        while weiter != "n" or weiter != "j":
            weiter = input("Möchten Sie noch mal spielen? (j/n): ")
            if weiter == "n":
                spielen = False
                break
            elif weiter == "j":
                 zaehler == 0
                 break
            else:
                 print("\nIch habe nicht verstanden, bitte Geben Sie j oder n ein: ")
    else:
        zaehler +=1                              # jeder Versuch erhöht den Zähler um 1
        if zahl_zu_erraten > rate:
            print("\n",niedrig,"Das war",zaehler,"Versuch")
        else:
            print("\n",hoch,"Das war",zaehler,"Versuch")