import time


def intro_game(size, computer, player_boats, computer_boats):
    time.sleep(2)
    print("\nOhh! Long time waiting for this!")
    time.sleep(1)
    print("\nBefore get started, let me ask you...\n")
    time.sleep(1)
    shirt = input("\nWhat color is your ugly shirt?\n")
    while True:
        if shirt.isdigit():
            print(f"\nI don`t think '{shirt}' reffers to any color boy!")
            print("\nTry again!")
            shirt = input("\n")
        elif len(shirt) < 3:
            print("\nThat is way to short...try again")
            shirt = input("\n")
        elif len(shirt) > 6:
            print("\nThat is way to long...try again")
            shirt = input("\n")
        else:
            break
    time.sleep(1)
    food = input("\n...and what did you last have for food?\n")
    while True:
        if food.isdigit():
            print("\nAll names must be made of alphabetic characters boy!")
            time.sleep(1)
            print("\nTry again!")
            food = input("\n")
        elif len(food) < 4:
            time.sleep(1)
            print("\nThat is way to short...try again")
            food = input("\n")
        elif len(food) > 9:
            print("\nThat is way to long...try again")
            shirt = input("\n")
        else:
            break

    player_name = shirt + food
    player_name = player_name.capitalize()
    print("\nI always like to know my adversary's name")
    time.sleep(1)
    print(f"\nI will put you to the ground {player_name}!")
    time.sleep(2)
    print("\nCheck this out for now...")
    time.sleep(2)
    print("\n----------------------------")
    print("          Players           ")
    print(f" Computer         {player_name}\n")
    print("       Number of ships      ")
    print(f"    {computer_boats}                  {player_boats}\n  ")
    print("----------------------------")
    time.sleep(2)
    if computer_boats and player_boats != 5:
        pass
    else:
        print("\noohh seems we don't have all the boats available right now...")
        time.sleep(1)
        print("\n... but we will fight anyway!")
        time.sleep(2)
    print("\n   +++++++++++++++++++")
    print("          LEYEND        ")
    print("    S = boats           ")
    print("    X = water           ")
    print("    $ = hit/shunk       ")
    print("   ++++++++++++++++++++")
    time.sleep(3)
    print(f"\nGood luck {player_name}")
    time.sleep(1)
    print("\nI will lend you a radar...")
    time.sleep(2)
    print("\n    Radar")
    print("  1 2 3 4 5")
    computer.populate_board("computer", size)
    print("\nand i will let you shot first!")
    time.sleep(1)
    print(f"\nI will see you in abism {player_name}!")
    time.sleep(2)
    return player_name
