import random
from random import randint
from pprint import pprint


class Board:
    """
    Define game's board
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["-" for i in range(size)] for row in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
        

    def print(self):
        for row in self.board:
            board = " ".join(row)
        for landpoint in range(1, 9):
            print(landpoint, board)


    def column_cordenates():
        translate_cordenates = {
            "a" : 0, "b": 1, "c": 2, "d": 3, "f": 4, "g": 5, "h": 6, "i": 7
            }
        return translate_cordenates

    
    def random_ship(self, size):
        total_ships = 0
        while total_ships <= 5:
            x = random.randint(0, size)
            y = random.randint(0, size)
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
    


def main():
    size = 8
    board = Board(size, size, "Javier", "user")
    game_board = board.print()
    random_ship = board.random_ship(size)
    print(random_ship)
    # user_guess = input("Take your shot\n")
    print(board.user_guess())
print("  A B C D F G H I")
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
