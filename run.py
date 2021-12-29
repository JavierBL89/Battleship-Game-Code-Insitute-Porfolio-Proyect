import random
import time
import random
from typing import Sized


class Board:
    """
    Define game's players objects, game battleships,
    and define lists of ships and shots used
    during the game.
    """
    def __init__(self, size, board, name, type):
        self.size = size
        self.name = name
        self.type = type
        self.board = [["-" for i in range(1, size)] for row in range(1, size)]
        self.guesses = []
        self.ships = []
        self.player_shots = []
        self.computer_shots = []
        self.player_ships = [(7, 5), (4, 5), (0, 3)]
        self.computer_ships = [(7, 5), (6, 5), (0, 3), (2, 0), (7, 2)]


    def random_ship(self, size, type):
        """
        Create 5 random ships for each player
        """
        total_ships = 1
        while total_ships <= 5:
            x = random.randint(1, size) 
            y = random.randint(1, size) 
            if type == "computer":
                self.computer_ships.append((x, y))
            elif type == "player":
                self.player_ships.append((x, y))
            total_ships += 1
        return self.ships

    def player_guess(self):
        """
        Takes user input and validates data
        Raise and erro if data in not valid
        """
        try:
            print("\nYou shot!")
            guess_row = int(input("\nRow: "))
            while guess_row not in [ 1, 2, 3, 4, 5, 6, 7, 8]:
                print("Please enter  valid data, only whole numbers from 1 to 8 are valid!\n")
                guess_row = int(input("Row: "))

            guess_column = int(input("Column: "))
            while guess_column not in [ 1, 2, 3, 4, 5, 6, 7, 8]:
                print("Please enter  valid data, only whole numbers from 1 to 8 are valid!\n")
                guess_column = int(input("Column: ")) 
        except ValueError:
            print("No a valid input")
            self.player_guess()
        return guess_row, guess_column

    
    def computer_guess(self):
        """
        Creates computer random shots
        """
        # self.x = random.randint(1, 8)
        # self.y = random.randint(1, 8)
        self.x = 7
        self.y = 5
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
            self.row = player_shot[0]
            self.column = player_shot[1]
            if player_shot not in self.computer_ships:
                self.board[self.row][self.column] = "X"
            elif player_shot in self.computer_ships:
                self.board[self.row][self.column] = "$"
            return self.board
        elif player_shot in self.player_shots:
            row, col = player_shot
            row += 1
            col += 1
            print(f"Coordenates {row, col} already been used")
            print("Shot again!")
            self.player_guess()
            
    def check_guess_2(self, computer_shot):
        for boat in self.player_ships:
            self.x = boat[0]
            self.y = boat[1]
            self.board[self.x][self.y] = "S"
        self.row = computer_shot[0]
        self.column = computer_shot[1]
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
            # for boat in self.player_ships:
            #     self.x = boat[0]
            #     self.y = boat[1]
            #     self.board[self.x][self.y] = "S"
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
                print("\n...I'll be waiting for you to come back...right here!")
                time.sleep(1)
                print("\nThis man is full of him self!")
                restart = input("\nYou wanna try and give him hell? y/n\n")
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
    

def play_game(computer, player, size):
    """
    Start up game and run till the end of it
    """
    # print("\nOhh! Long time waiting for this!")
    # time.sleep(1)
    # print("\nBefore get started, let me ask you...\n")
    # time.sleep(1)
    # shirt = input("\nWhat color is your ugly shirt\n?")
    # time.sleep(1)
    # print("\nahgg!! Really ugly")
    # time.sleep(1)
    # food = input("\n...and what did you last have for food?\n")
    # player_name = shirt + food
    # player_name = player_name.capitalize()
    # print("\nI always like to know my adversary's name")
    # time.sleep(1)
    # print(f"\nI will put you to the ground {player_name}!")
    # time.sleep(2)
    # print("\nCheck this out for now...")
    # time.sleep(2)
    # print("\n----------------------------")
    # print("          Players           ")
    # print(f" Computer         {player_name}\n")
    # print("       Number of ships      ")
    # print("    5                  5\n  ")
    # print("           Score            ")
    # print("    0                  0    ")
    # print("----------------------------")
    # time.sleep(4)
    # print("\n   +++++++++++++++++++")
    # print("          LEYEND        ")
    # print("    S = boats           ")
    # print("    X = water           ")
    # print("    $ = hit/shunk       ")
    # print("   ++++++++++++++++++++")
    # time.sleep(3)
    # print("\n...your game board")
    # time.sleep(1)
    # print(f"\n     {player_name}")
    # print("  A B C D F G H I")
    # player.populate_board("player", size)
    # time.sleep(4)
    # print(f"\n...Today's your lucky day {player_name}")
    # time.sleep(1)
    # print("\n....I will lend you a radar...")
    # time.sleep(2)
    # print("\n     Radar")
    # print("  A B C D F G H I")
    # computer.populate_board("computer", Sized)
    # print("\n...and i will let you shot first!")
    # time.sleep(1)
    # print(f"\n...I will see you in abism {player_name}!")
    # time.sleep(2)
    game = True
    while game:

        # computer.random_ship(size, "computer")
        # player.random_ship(size, "player")
        
        player_shot = player.player_guess()
        computer_shot = computer.computer_guess()
        time.sleep(1)
        count = player.validate_shot(player_shot, "player")
        time.sleep(2)
        print(f"\nMy shot is... {computer_shot}")
        time.sleep(2)
        count = computer.validate_shot(computer_shot, "computer")
        time.sleep(1)
        player.check_guess_2(computer_shot)
        # print(f"     {player_name}")
        print("  1 2 3 4 5 6 7 8")
        player.populate_board("player", computer_shot)
        game = Board.game_over(count)
        if game is False:
            
            break
        time.sleep(1)
        computer.check_guess(player_shot)
        print("\n      Radar    ")
        print("  1 2 3 4 5 6 7 8")
        computer.populate_board("computer", player_shot)
        game = Board.game_over(count)
        if game is False:
            print("I knew i could beat you!\n")
            print("Pricks like you must be erased of this unfilthy planet...\n")
            break
        else:
            game = True


def main():
    size = 9
    computer = Board(size, size, "Titanico", "computer")
    player = Board(size, size, "Javier", "user")
    play_game(computer, player, size)


main()