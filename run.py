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

current_user_answer = []

def get_answers_survey():
    """ 
    Access to the survey worksheet
    Show questions to the user and get user's answers
    """
    print("Hey Captain, great to have to someone to beat to!\n")
    print("Before beating you, I'd like you to participate in a quick gaming survey.\n")
    start_survey = input("Ready to answer 4 simple questions? Y/N\n").upper()
     
    survey_data = SHEET.worksheet("survey")
    questions = survey_data.get_all_values()
    
    global current_user_answer
    if start_survey == "Y":

        while True:
            for question in questions:
                print(f"{question[0]}")
                answer_1 = input().lower()
                if not validate_data(answer_1, question[0]):
                    break
                print(f"{question[1]}\n every week | twice a month | once in a while")
                answer_2 = input().lower()
                if not validate_data(answer_2, question[1]):
                    break
                print(f"{question[2]}\n computer | video console | both alike")
                answer_3 = input().lower()
                if not validate_data(answer_3, question[2]):
                    break   
                print(f"{question[3]}\n strategy | shooting | sports")
                answer_4 = input().lower()
                if not validate_data(answer_4, question[3]):
                    break
                # elif validate_data(answer_4, question[3]):  
                print(current_user_answer)

                time.sleep(2)                
                print("LET THE BATTLE BEGIN")
                time.sleep(2)
                exit()

def validate_data(answer, question):
    choises = ["male", "female", "every week", "twice a month", " once in a while", "computer", "video console", "both alike", "strategy", "shooting", "sports"]
    try:
        current_user_answer.append(answer)
        if answer not in choises:
            current_user_answer.clear()
            print(current_user_answer)
            raise ValueError(
                "sorry! you must select one of the given options.\n")
            
    except ValueError as e:
        print(f"Invalid answer {e}, Please try again.")
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

