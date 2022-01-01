import time
import sys
from run import restart_game

def restart_loop(shooter):
    if shooter == "computer":
        restart = input("\nYou wanna try and give him hell? 'y/n'\n")
        while True:
            restart.lower()
            if restart == "y":
                restart_game()
            elif restart == "n":
                print("I guess you must need a break..")
                print("See ya soon boy!")
                sys.exit()
            elif restart != "y" or restart != "n":
                print("\nYou must enter a valid answer 'y/n'")
                time.sleep(1)
                restart = input("\nYou wanna try again "
                                "and give him hell? 'y/n'\n")
                restart.lower()
    elif shooter == "player":
        restart = input("\nYou wanna try and give him hell? 'y/n'\n")
        while True:
            restart.lower()
            if restart == "y":
                restart_game()
            elif restart == "n":
                print("I guess you must need a break..")
                print("See ya soon boy!")
                sys.exit()
            elif restart != "y" or restart != "n":
                print("\nYou must enter a valid answer 'y/n'")
                time.sleep(1)
                restart = input("\nYou wanna try again "
                                "and give him hell? 'y/n'\n")
                restart.lower()