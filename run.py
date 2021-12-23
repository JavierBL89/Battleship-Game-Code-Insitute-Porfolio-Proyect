import random
from random import randint
from pprint import pprint


class Board:
    """
    Define game's board
    """
    def __init__(self, size, board, name, type):
        self.size = size
        self.name = name
        self.type = type
        self.board = [["-" for i in range(1, size)] for row in range(1, size)]
        self.guesses = []
        self.ships = []
        self.user_shots = []
        self.computer_shots = []
               

    def column_cordenates():
        translate_cordenates = {
            "a" : 0, "b": 1, "c": 2, "d": 3, "f": 4, "g": 5, "h": 6, "i": 7
            }
        return translate_cordenates

    
    def random_ship(self, size):
        total_ships = 0
        while total_ships <= 5:
            x = random.randint(1, size)
            y = random.randint(1, size)
            self.ships.append((x, y))
            total_ships += 1
        return self.ships

    def user_guess(self):
        try:
            guess_row = int(input("Row: "))
            while guess_row > randint(1,9):
                print("Please enter  valid data, only whole numbers from 1 to 9 are valid!\n")
                guess_row = int(input("Row: "))

            guess_column = int(input("Column: "))
            while guess_column > randint(1,9):
                print("Please enter  valid data, only whole numbers from 1 to 9 are valid!\n")
                guess_column = int(input("Column: "))
            
        except ValueError:
            print("No a valid input")
        return guess_row, guess_column

   
    def computer_guess(self):
        x = random.randint(1,9)
        y = random.randint(1,9)
        compu_guess = x, y 
        if compu_guess not in self.computer_shots:
            self.computer_shots.append(compu_guess)
        elif compu_guess in computer_shots:
            computer_guess()
        print(x, y)


    def check_guess(self, player_guess):
        if player_guess not in self.user_shots:
            self.user_shots.append(player_guess)
            self.row = player_guess[0]
            self.column = player_guess[1]
            self.board[self.row][self.column] = "X"
            return self.board
        elif player_guess in user_shots:
            print(f"Coodenates {player_guess} already used")
            user_guess()
        

    def populate_board(self):
        
        for row in self.board:
            board = " ".join(row)
            print(board)


def main():
    size = 9
    computer = Board(size, size, "Titanico", "user")
    player = Board(size, size, "Javier", "user")

    random_computer_ship = computer.random_ship(size)
    random_player_ship = player.random_ship(size)
    
    print(random_player_ship)
    print(random_computer_ship)

    computer_guess = computer.computer_guess()
    player_guess = player.user_guess()

    radar = computer.check_guess(player_guess)
    print("  A B C D F G H I")
    computer.populate_board()
    print(" My Battleship")
    player.populate_board()
    

    


main()







# import random
# import time
# import gspread
# from google.oauth2.service_account import Credentials

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# CREDS = Credentials.from_service_account_file("creds.json")
# SCOPE_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
# SHEET = GSPREAD_CLIENT.open("Gaming_survey")

# current_user_answer = []

# def get_answers_survey():
#     """ 
#     Access to the survey worksheet
#     Show questions to the user and get user's answers
#     """
#     print("Hey Captain, great to have to someone to beat to!\n")
#     print("Before beating you, I'd like you to participate in a quick gaming survey.\n")
#     start_survey = input("Ready to answer 4 simple questions? Y/N\n").upper()
     
#     survey_data = SHEET.worksheet("survey")
#     questions = survey_data.get_all_values()
    
#     global current_user_answer
#     if start_survey == "Y":

#         while True:
#             for question in questions:
#                 print(f"{question[0]}")
#                 answer_1 = input().lower()
#                 if not validate_data(answer_1, question[0]):
#                     break
#                 print(f"{question[1]}\n every week | twice a month | once in a while")
#                 answer_2 = input().lower()
#                 if not validate_data(answer_2, question[1]):
#                     break
#                 print(f"{question[2]}\n computer | video console | both alike")
#                 answer_3 = input().lower()
#                 if not validate_data(answer_3, question[2]):
#                     break   
#                 print(f"{question[3]}\n strategy | shooting | sports")
#                 answer_4 = input().lower()
#                 if not validate_data(answer_4, question[3]):
#                     break
#                 # elif validate_data(answer_4, question[3]):  
#                 print(current_user_answer)

#                 time.sleep(2)                
#                 print("LET THE BATTLE BEGIN")
#                 time.sleep(2)
#                 exit()

# def validate_data(answer, question):
#     choises = ["male", "female", "every week", "twice a month", " once in a while", "computer", "video console", "both alike", "strategy", "shooting", "sports"]
#     try:
#         current_user_answer.append(answer)
#         if answer not in choises:
#             current_user_answer.clear()
#             print(current_user_answer)
#             raise ValueError(
#                 "sorry! you must select one of the given options.\n")
            
#     except ValueError as e:
#         print(f"Invalid answer {e}, Please try again.")
#         return False

#     return True


# get_answers_survey()
