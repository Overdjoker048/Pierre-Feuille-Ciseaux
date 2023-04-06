import random
import os
import colorama
import platform

class Item():
    def __init__(self, name, force):
        self.name = name
        self.force   = force

colorama.init()
print(colorama.Fore.GREEN)

if platform.system() == "Windows":
    os.system("title Rock Paper Scissors")
elif platform.system() == "Linux":
    os.system("sudo apt-get install xtitle")
    os.system("xtitle 'Rock Paper Scissors'")
elif platform.system() == "Darwin":
    os.system("touch 'Rock Paper Scissors'")

items = [Item(name="rock", force="scissors"), Item(name="paper", force="rock"), Item(name="scissors", force="paper")]
win = 0
loose = 0

while True:
    gui = f""" _____            _      _____                        _____       _                          
| __  | ___  ___ | |_   |  _  | ___  ___  ___  ___   |   __| ___ |_| ___  ___  ___  ___  ___ 
|    -|| . ||  _|| '_|  |   __|| .'|| . || -_||  _|  |__   ||  _|| ||_ -||_ -|| . ||  _||_ -|
|__|__||___||___||_,_|  |__|   |__,||  _||___||_|    |_____||___||_||___||___||___||_|  |___|
                                |_|                                                      
Victory: {win} Defeat: {loose}

[*] Rock
[*] Paper
[*] Scissors
"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("reset")
    elif platform.system() == "Darwin":
        os.system("clear")
    print(gui)
    choice = input("[Game] What do you want to play:\n>>>").lower().replace(" ", "")
    check = False
    for item in items:
        if choice == item.name:
            check = True
            break

    if check:
        print(f"\n[You] {choice}")
        choice_pourcent = random.randint(0, 2)
        if choice_pourcent == 0:
            for item in items:
                if choice == item.force:
                    print(f"[Computer] {item.name}.")
                    print("[Game] You loose")
                    loose += 1
        elif choice_pourcent == 1:
            print(f"[Computer] {choice}.")
            print("[Game] You equalized")
        
        elif choice_pourcent == 2:
            for item in items:
                if choice == item.name:
                    print(f"[Computer] {item.force}")
                    print("[Game] You win !")
                    win += 1
    else:
        print("\n[Error] What you entered is not part of the expected answers.")
    
    input("\n[Game] Press Enter to restart...")
