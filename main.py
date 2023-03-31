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
            choice_pourcent = random.randint(0, 100)
            if choice_pourcent <= 33:
                for item in items:
                    if choice == item.force:
                        print(f"[Ordinateur] {item.name}.")
                        print("Tu as perdu.")
                        input("Appuyé sur entrer pour rejouer...")
                        if sys.platform == "win32":
                            os.system("cls")
                        else:
                            os.system("clear")
            elif choice_pourcent <= 66:

                print(f"[Ordinateur] {choice}.")
                print("Tu as fais égalité.")
                input("Appuyé sur entrer pour rejouer...")
                if sys.platform == "win32":
                    os.system("cls")
                else:
                    os.system("clear")
            
            elif choice_pourcent <= 100:
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