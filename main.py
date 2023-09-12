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

match platform.system():
    case "Windows": 
        os.system("title Rock Paper Scissors")
        clear_cmd = "cls"
    case "Linux":
        os.system("sudo apt-get install xtitle")
        os.system("xtitle 'Rock Paper Scissors'")
        clear_cmd = "reset"
    case "Darwin":
        os.system("touch 'Rock Paper Scissors'")
        clear_cmd = "clear"

items = [Item(name="rock", force="scissors"), Item(name="paper", force="rock"), Item(name="scissors", force="paper")]
win = 0
loose = 0

try:
    while True:
        os.system(clear_cmd)
        print(f"""     _____            _      _____                        _____       _                          
    | __  | ___  ___ | |_   |  _  | ___  ___  ___  ___   |   __| ___ |_| ___  ___  ___  ___  ___ 
    |    -|| . ||  _|| '_|  |   __|| .'|| . || -_||  _|  |__   ||  _|| ||_ -||_ -|| . ||  _||_ -|
    |__|__||___||___||_,_|  |__|   |__,||  _||___||_|    |_____||___||_||___||___||___||_|  |___|
                                        |_|                                                      
    Victory: {win} Defeat: {loose}

    [*] Rock
    [*] Paper
    [*] Scissors
    """)
        choice = input("[Game] What do you want to play:\n>>>").lower().replace(" ", "")
        check = False
        for item in items:
            if choice == item.name:
                check = True
                break

        if check:
            print(f"\n[You] {choice.title()}")
            match random.randint(0, 2):
                case 0:
                    for item in items:
                        if choice == item.force:
                            print(f"[Computer] {item.name.title()}")
                            print("[Game] You loose")
                            loose += 1
                            break
                case 1:
                    print(f"[Computer] {choice.title()}")
                    print("[Game] You equalized")
                
                case 2:
                    for item in items:
                        if choice == item.name:
                            print(f"[Computer] {item.force.title()}")
                            print("[Game] You win !")
                            win += 1
                            break
        else:
            print("\n[Error] What you entered is not part of the expected answers.")
        
        input("\n[Game] Press Enter to restart...")
except KeyboardInterrupt:
    print("\nGood Bye :)")