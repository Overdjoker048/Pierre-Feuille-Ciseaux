import random
import platform
import os

match platform.system():
    case "Windows":
        clear_cmd = "cls"
    case _:
        clear_cmd = "clear"

items = {
    "Rock": ["Paper", "Scissors"],
    "Paper": ["Scissors", "Rock"],
    "Scissors": ["Rock", "Paper"]
}
win = 0
loose = 0

try:
    while True:
        os.system(clear_cmd)
        print(f""" _____            _      _____                        _____       _
| __  | ___  ___ | |_   |  _  | ___  ___  ___  ___   |   __| ___ |_| ___  ___  ___  ___  ___ 
|    -|| . ||  _|| '_|  |   __|| .'|| . || -_||  _|  |__   ||  _|| ||_ -||_ -|| . ||  _||_ -|
|__|__||___||___||_,_|  |__|   |__,||  _||___||_|    |_____||___||_||___||___||___||_|  |___|
                                        |_|
    Victory: {win} Defeat: {loose}

    [*] Rock
    [*] Paper
    [*] Scissors
    """)
        choice = input("[Game] What do you want to play:\n>>>").replace(" ", "").title()
        check = False
        for item in items:
            if choice == item.name:
                check = True
                break

        if check:
            print(f"\n[You] {choice}")
            choice_pourcent = random.randint(0, 2)
            match choice_pourcent:
                case 0:
                    for item in items:
                        if choice == item.force:
                            print(f"[Computer] {item.name}")
                            print("[Game] You loose")
                            loose += 1
                case 1:
                    print(f"[Computer] {choice}")
                    print("[Game] You equalized")
                case 2:
                    for item in items:
                        if choice == item.name:
                            print(f"[Computer] {item.force}")
                            print("[Game] You win !")
                            win += 1
        else:
            print("\n[Error] What you entered is not part of the expected answers.")

        input("\n[Game] Press Enter to restart...")
except KeyboardInterrupt:
    print("\n\nGood Bye :)")
