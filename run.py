import random
import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open("Gaming_survey")


def get_answers_survey():
    
    
    print("Hey Captain, great to have to someone to beat to!\n")
    print("Before beating you, I'd like you to participate in a quick gaming survey.\n")
    start_survey = input("Ready to answer 4 simple questions? Y/N\n").upper()
     
    survey_data = SHEET.worksheet("survey")
    questions = survey_data.get_all_values()

    if start_survey == "Y":

        while True:
            for question in questions:
                print(f"{question[0]}")
                answer_1 = input().lower()
                validate_data(answer_1, question)
    
                print(f"{question[1]}")
                print("every week | twice a month | once in a while")
                answer_2 = input().lower()
                validate_data(answer_2, question[1])
    
                print(f"{question[2]}")
                print("computer | video console | both alike")
                answer_3 = input().lower()
                validate_data(answer_3)
    
                print(f"{question[3]}")
                print("strategy | shooting | sports")
                answer_4 = input().lower()
                validate_data(answer_4)
    
                time.sleep(2)
                print("LET THE BATTLE BEGIN")
                time.sleep(2)


def validate_data(answer, question):
    choises = ["male", "female", "every week", "twice a month", " once in a while", "computer", "video console", "both alike", "strategy", "shooting", "sports"]
    try:
        if answer is not choises:
            raise ValueError(
                "sorry! you must select one of the given options.\n")
            
    except ValueError as e:
        print(f"Invalid answer {e}, Please try again.")
        print(f"{question}")
        return False

    return True


get_answers_survey()



# class Question
#     def __init__(self, question, a ,b , c):
#         self.question = question
#         self.a = a 
#         self.b = b 
#         self.c = c

# question_1 = Question()