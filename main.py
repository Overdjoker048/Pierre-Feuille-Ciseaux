from item import Item
import random
import sys
import os

items = [Item(name="pierre", force="ciseaux"), Item(name="feuille", force="pierre"), Item(name="ciseaux", force="feuille")]

try:
    while True:
        choice = input("Pierre, feuille ou ciseaux ?").lower().replace(" ", "")
        check = False
        for item in items:
            if choice == item.name:
                check = True
                break
        
        if check:
            print(f"[Joueur] {choice}")
            if random.randint(0, 100) <= 60:
                for item in items:
                    if choice == item.force:
                        print(f"[Ordinateur] {item.name}.")
                        print("Tu as perdu.")
                        input("Appuyé sur entrer pour rejouer...")
                        if sys.platform == "win32":
                            os.system("cls")
                        else:
                            os.system("clear")
            else:
                for item in items:
                    if choice == item.name:
                        print(f"[Ordinateur] {item.force}")
                        print("Tu as gagné.")
                        input("Appuyé sur entrer pour rejouer...")
                        if sys.platform == "win32":
                            os.system("cls")
                        else:
                            os.system("clear")
        else:
            print("[Erreur] Ce que vous avez entrez ne fais pas partie des réponses attendues.")
except KeyboardInterrupt:
    print("\nA la prochaine :)")