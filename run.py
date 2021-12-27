import random
import time
from random import randint
from pprint import pprint


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
        # self.count = 0
        self.guesses = []
        self.ships = []
        self.player_shots = []
        self.computer_shots = []
        self.player_ships = [(7, 5), (4, 5), (0, 3)]
        self.computer_ships = [(7, 5), (6, 5), (0, 3), (2, 0), (7, 
2)]
               

    def column_cordenates():
        translate_cordenates = {
            "a" : 0, "b": 1, "c": 2, "d": 3, "f": 4, "g": 5, "h": 6, "i": 7
            }
        return translate_cordenates


    def random_ship(self, size, type):
        """
        Create 5 random ships for each player
        """
        total_ships = 1
        while total_ships <= 5:
            x = random.randint(0, size) - 1
            y = random.randint(0, size)- 1
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
            while guess_row not in [0,1,2,3,4,5,6,7]:
                print("Please enter  valid data, only whole numbers from 1 to 9 are valid!\n")
                guess_row = int(input("Row: "))

            guess_column = int(input("Column: "))
            while guess_column not in [0,1,2,3,4,5,6,7]:
                print("Please enter  valid data, only whole numbers from 1 to 9 are valid!\n")
                guess_column = int(input("Column: "))
            
        except ValueError:
            print("No a valid input")
            self.player_guess()
        return guess_row, guess_column

    
    def computer_guess(self):
        """
        Creates computer random shots
        Updates the players battleship accordingly
        """
        # self.x = random.randint(0,7)
        # self.y = random.randint(0,7)
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
            self.row = player_shot[0]
            self.column = player_shot[1]
            self.player_shots.append(player_shot)
            if player_shot not in self.computer_ships:
                self.board[self.row][self.column] = "X"
            elif player_shot in self.computer_ships:
                self.board[self.row][self.column] = "$"
            return self.board
        elif player_shot in self.player_shots:
            print(f"Coordenates {player_shot} already been used")
            print("Shot again!")
            self.player_guess()
        

    def populate_board(self, player, shot):
        """
        Populates neatly the battleship passed in
        """
        # self.guess_x = self.computer_shots[0]
        # self.guess_y = self.computer_shots[0]

        row_number = 0
        if player == "player": 
            for boat in self.player_ships:
                self.x = boat[0]
                self.y = boat[1]
                self.board[self.x][self.y] = "S"
                if shot in self.player_ships:
                    self.board[shot[0]][shot[1]] = "$"
            # print(self.guess_x)

            # for shot in self.computer_shots:
            #     self.x = shot[0]
            #     self.y = shot[1]
            #     self.board[self.x][self.y] = "$"
            # 
            for row in self.board:
                # while self.computer_shots in self.player_ships:
                #     row[self.guess_x][self.guess_y] = "$"
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
            print("\nYou shunk my boat motherfucker!")
        elif shooter == "player" and shot not in self.computer_ships:
            print("\nYou missed!")
        elif shooter == "computer" and shot in self.player_ships:
            count += 1
            print("Got you!")
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
        game = True
        while game:
            # computer.random_ship(size, "computer")
            # player.random_ship(size, "player")
            
            player_shot = player.player_guess()
            computer_shot = computer.computer_guess()
            computer.check_guess(player_shot)
            print("\n  Computer Radar")
            print("  A B C D F G H I")
            computer.populate_board("computer", player_shot)
            count = computer.validate_shot(player_shot, "player")
            game = Board.game_over(count)
            if game is False:
                print("""Well well well little bitch!!\n
You win this time...\n
I'll come back stronger and fuck your pretty ass!!\n""")
                break
            print(f"\nMy shot is... {computer_shot}")
            time.sleep(2)
            print("\n   My Battleship")
            print("  A B C D F G H I")
            player.populate_board("player", computer_shot)
            count = player.validate_shot(computer_shot, "computer")
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
    Board.play_game(computer, player, size)


main()