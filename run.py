import random
import time
import random
import sys
from modules.intro import intro_game
player_name = ""
player_boats = 0
computer_boats = 0


class Board:
    """
    Define game's players objects, game battleships,
    and define lists of ships and shots used
    during the game.
    """
    def __init__(self, size, name):
        self.size = size
        self.board = [["-" for i in range(size)] for row in range(size)]
        self.player_shots = []
        self.computer_shots = []
        self.player_ships = []
        self.computer_ships = []

    def random_ship(self, size, name):
        """
        Create 5 random ships for each player
        As duplicate boats, make a set of the lists 
        to get actual length of boats and keep track of them
        """
        global player_boats
        global computer_boats
        total_ships = 1
        while total_ships <= 5:
            x, y = random.randint(1, size), random.randint(1, size)
            if name == "computer":
                self.computer_ships.append((x, y))
                computer_boats = len(set(self.computer_ships))
            if name == "player":
                self.player_ships.append((x, y))
                player_boats = len(set(self.player_ships))
            total_ships += 1

    def player_guess(self):
        """
        Takes user input and validates data
        Raise and erro if data in not valid
        """
        guess_column = ""
        guess_row = ""
        try:
            print("\nYou shot!")
            guess_row = int(input("\nRow: "))
            while guess_row not in [1, 2, 3, 4, 5]:
                print("Please enter  valid data, "
                      "only whole numbers from 1 to 8 are valid!\n")
                guess_row = int(input("Row: "))

            guess_column = int(input("Column: "))
            while guess_column not in [1, 2, 3, 4, 5]:
                print("Please enter  valid data, "
                      "only whole numbers from 1 to 8 are valid!\n")
                guess_column = int(input("Column: "))
        except ValueError:
            print("No a valid input")
            self.player_guess()
        return guess_row, guess_column

    def computer_guess(self):
        """
        Creates computer random shots
        """
        self.x = random.randint(1, 5)
        self.y = random.randint(1, 5)
        compu_guess = self.x, self.y
        while compu_guess not in self.computer_shots:
            self.computer_shots.append(compu_guess)
            if compu_guess in self.computer_shots:
                self.computer_guess()
        return compu_guess

    def check_guess(self, player_shot):
        """
        Check user's shot against computer battleship
        Updates computer's battleship accordingly
        """
        if player_shot not in self.player_shots:
            self.player_shots.append(player_shot)
            self.row = player_shot[0] - 1
            self.column = player_shot[1] - 1
            if player_shot not in self.computer_ships:
                self.board[self.row][self.column] = "X"
            elif player_shot in self.computer_ships:
                self.board[self.row][self.column] = "$"
            return self.board
        elif player_shot in self.player_shots:
            row, col = player_shot
            print(f"\nCoordenates {row, col} already been used")
            print("Shot again!")
            self.player_guess()

    def check_guess_2(self, computer_shot):
        self.row = computer_shot[0] - 1
        self.column = computer_shot[1] - 1
        if computer_shot not in self.player_ships:
            self.board[self.row][self.column] = "X"
        return self.board

    def populate_board(self, player, shot):
        """
        Populates neatly the battleship passed in
        """
        global player_boats
        row_number = 0
        if player == "player":
            for boat in self.player_ships:
                self.x = boat[0] - 1
                self.y = boat[1] - 1
                self.board[self.x][self.y] = "S"
            if shot in self.player_ships:
                x = shot[0] - 1
                y = shot[1] - 1
                self.board[x][y] = "$"
            for row in self.board:
                board = " ".join(row)
                row_number += 1
                print(row_number, board)
        elif player == "computer":
            for row in self.board:
                board = " ".join(row)
                row_number += 1
                board = " ".join(row)
                print(row_number, board)

    def validate_shot(self, shot, shooter):
        """
        Validates whether the shot is hit or missed
        Response accordigly to the user
        """
        global player_boats
        global computer_boats
        if shooter == "player" and shot in self.computer_ships:
            computer_boats -= 1
            if computer_boats == 0:
                time.sleep(2)
                print("""\nWell well well little bitch!!\n
You win this time round...
""")
                time.sleep(2)
                print("\nYou think you're brave??")
                time.sleep(1)
                restart = input("\n..then give me another chance...'y/n'\n")
                while True:
                    restart.lower()
                    if restart == "y":
                        restart_game()
                    elif restart == "n":
                        time.sleep(1)
                        print("Nooo??! you little pussy!!")
                        time.sleep(1)
                        print("\nI will come back stronger then!")
                        time.sleep(1)
                        print("\nSee ya soon boy!")
                        sys.exit()
                    elif restart != "y" or restart != "n":
                        print("\nYou must enter a valid answer 'y/n'")
                        time.sleep(1)
                        restart = input("\ngive me another chance...'y/n'\n")
                        restart.lower()
            else:
                print("\nYou shunk my boat motherfucker!")
            return computer_boats
        elif shooter == "player" and shot not in self.computer_ships:
            print("\nYou missed!")
        elif shooter == "computer" and shot in self.player_ships:
            player_boats -= 1
            if player_boats == 0:
                print("\n..oohhh what a great feeling...")
                time.sleep(1)
                print("\nI win this time round!")
                time.sleep(1)
                print("\nWatch me enjoying the victory's smoke..")
                time.sleep(1)
                print("\n...I'll be waiting for you "
                      "to come back...right here!")
                time.sleep(2)
                print("\nThis man is full of him self!")
                restart = input("\nLet's try again and give him hell! 'y/n'\n")
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
            else:
                print("\nah aaah!!")
                time.sleep(1)
                print("\nGot you!")
            return player_boats
        elif shooter == "computer" and shot not in self.player_ships:
            print("\nMissed!...\n")

    def game_over(boats):
        if boats == 0:
            return False


def restart_game():
    global player_name
    time.sleep(1)
    print(f"\n...glad to see back {player_name}")
    time.sleep(1)
    print("\n...thought you'd run away like a rat!")
    time.sleep(1)
    print("\nhere a hint...")
    print("\n...some boats might be next to one another...")
    time.sleep(1)
    print("\nI will let you shot first!")
    print("\n...consider it as a profesional courtesy...")
    time.sleep(1)
    main()


def play_game(computer, player, player_game, size):
    """
    Start up game and run till the end of it
    """
    global player_boats
    global computer_boats

    game = True
    while game:
        player_shot = player.player_guess()
        computer_shot = computer.computer_guess()
        time.sleep(1)
        computer.check_guess(player_shot)
        player_win = computer.validate_shot(player_shot, "player")
        computer_count = Board.game_over(player_win)
        if computer_count is False:
            break
        else:
            compu_boats = True
        time.sleep(2)
        print(f"\nMy shot is... {computer_shot}")
        time.sleep(2)
        computer_wins = player.validate_shot(computer_shot, "computer")
        time.sleep(1)
        player.check_guess_2(computer_shot)
        print(f"{player_name}")
        print("...........")
        print("  1 2 3 4 5")
        player.populate_board("player", computer_shot)
        print(f"\nBoats left: {player_boats}")
        player_count = Board.game_over(computer_wins)
        if player_count is False:
            break
        else:
            player_count = True
        time.sleep(1)
        print("\n   Radar   ")
        print("...........")
        print("  1 2 3 4 5")
        computer.populate_board("computer", player_shot)
        print(f"\nBoats left: {computer_boats}")


def main():
    global player_name
    global player_boats
    global computer_boats
    size = 5

    computer = Board(size, "computer")
    player = Board(size, player_name)
    computer.random_ship(size, "computer")
    player.random_ship(size, "player")
    if not player_name:
        player_name = intro_game(size, computer, player_boats, computer_boats)
    else:
        pass
    play_game(computer, player, player_name, size)


main()
