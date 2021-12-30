import random
import time
import random
import sys
from intro import intro_game
player_name = ""


class Board:
    """
    Define game's players objects, game battleships,
    and define lists of ships and shots used
    during the game.
    """
    def __init__(self, size):
        self.size = size
        self.board = [["-" for i in range(size)] for row in range(size)]
        self.player_shots = []
        self.computer_shots = []
        self.player_ships = [(7, 5), (4, 5), (0, 3)]
        self.computer_ships = [(7, 5), (6, 5), (0, 3), (2, 0), (7, 2)]

    def random_ship(self, size, name):
        """
        Create 5 random ships for each player
        """
        total_ships = 1
        while total_ships <= 5:
            x = random.randint(1, size)
            y = random.randint(1, size)
            if name == "computer":
                self.computer_ships.append((x, y))
            elif name == "player":
                self.player_ships.append((x, y))
            total_ships += 1
        return self.ships

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
            while guess_row not in [1, 2, 3, 4, 5, 6, 7, 8]:
                print("Please enter  valid data, "
                      "only whole numbers from 1 to 8 are valid!\n")
                guess_row = int(input("Row: "))

            guess_column = int(input("Column: "))
            while guess_column not in [1, 2, 3, 4, 5, 6, 7, 8]:
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
        self.x = random.randint(1, 8)
        self.y = random.randint(1, 8)
        # self.x = 7
        # self.y = 5
        compu_guess = self.x, self.y
        if compu_guess not in self.computer_shots:
            self.computer_shots.append(compu_guess)
            return compu_guess
        elif compu_guess in self.computer_shots:
            self.computer_guess()

    def check_guess(self, player_shot):
        """
        Check user's shot against computer battleship
        Updates computer's battleship accordingly
        """
        if player_shot not in self.player_shots:
            self.player_shots.append(player_shot)
            self.row = int(player_shot[0]) - 1
            self.column = int(player_shot[1]) - 1
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
        for boat in self.player_ships:
            self.x = boat[0]
            self.y = boat[1]
            self.board[self.x][self.y] = "S"
        self.row = computer_shot[0] - 1
        self.column = computer_shot[1] - 1
        if computer_shot not in self.player_ships:
            self.board[self.row][self.column] = "X"
        elif computer_shot in self.player_ships:
            self.board[self.row][self.column] = "$"
        return self.board

    def populate_board(self, player, shot):
        """
        Populates neatly the battleship passed in
        """
        row_number = 0
        if player == "player":
            for row in self.board:
                board = " ".join(row)
                row_number += 1
                print(row_number, board)
        else:
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
        count = 0
        if shooter == "player" and shot in self.computer_ships:
            count += 1
            if count == 2:
                print("""\nWell well well little bitch!!\n
You win this time...\n
I'll come back stronger and fuck your pretty ass!!\n""")
            else:
                print("\nYou shunk my boat motherfucker!")
        elif shooter == "player" and shot not in self.computer_ships:
            print("\nYou missed!")
        elif shooter == "computer" and shot in self.player_ships:
            count += 1
            if count == 1:
                print("\n..oohhh what a great feeling...")
                time.sleep(1)
                print("\n...watch me enjoying the victory's smoke..")
                time.sleep(1)
                print("\n...I'll be waiting for you "
                      "to come back...right here!")
                time.sleep(1)
                print("\nThis man is full of him self!")
                restart = input("\nYou wanna try and give him hell? y/n\n")
                while not restart.lower() == "y" or restart.lower == "n":
                    print("\nYou must enter a valid answer 'y/n'")
                    time.sleep(1)
                    restart = input("\nYou wanna try again "
                                    "and give him hell? 'y/n'\n")
                if restart.lower == "y":
                    restart()
                elif restart.lower() == "n":
                    sys.exit()
            else:
                print("\nah aaah!!")
                time.sleep(1)
                print("\nGot you!")
        elif shooter == "computer" and shot not in self.player_ships:
            print("\nMissed!...\n")
        return count

    def game_over(count):
        if count == 1:
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


def play_game(computer, player, player_game):
    """
    Start up game and run till the end of it
    """
    game = True
    while game:
        # computer.random_ship(size, "computer")
        # player.random_ship(size, "player")

        player_shot = player.player_guess()
        computer_shot = computer.computer_guess()
        time.sleep(1)
        computer.check_guess(player_shot)
        count = player.validate_shot(player_shot, "player")
        time.sleep(2)
        print(f"\nMy shot is... {computer_shot}")
        time.sleep(2)
        count = computer.validate_shot(computer_shot, "computer")
        time.sleep(1)
        player.check_guess_2(computer_shot)
        print(f"     {player_name}")
        print("  1 2 3 4 5 6 7 8")
        player.populate_board("player", computer_shot)
        game = Board.game_over(count)
        if game is False:
            break
        time.sleep(1)
        print("\n      Radar    ")
        print("  1 2 3 4 5 6 7 8")
        computer.populate_board("computer", player_shot)
        game = Board.game_over(count)
        if game is False:
            print("I knew i could beat you!\n")
            print("Pricks like you must be erased "
                  "of this unfilthy planet...\n")
            break
        else:
            game = True


def main():
    size = 8
    computer = Board(size)
    player = Board(size)
    global player_name
    # player_name = intro_game(size, computer)
    play_game(computer, player, player_name)


main()
