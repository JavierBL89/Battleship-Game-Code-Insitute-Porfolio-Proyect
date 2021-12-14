import random
import time
import gspread
from pprint import pprint
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

user_answers = []


def start_survey():
    """ 
    Ask user whether or not participate in the survey
    Validate user data input
    """
    print("Hey Captain, great to have to someone to beat to!\n")
    print("Before beating you, I'd like you to participate in a quick gaming survey.\n")
    start_survey = input("Ready to answer 4 simple questions? Y/N\n").upper()
    
    if start_survey == "Y":
         main()
    elif start_survey == "N":
        print("LET THE BATTLE BEGIN!")
        exit()
    else:
        print("Please, select one of the choises given")


def get_answers_survey():
    """ 
    Access to the survey worksheet
    Show questions to the user and get user's answers
    """
    
    survey_data = SHEET.worksheet("survey")
    questions = survey_data.get_all_values()
    
    global user_answers
         
    while True:
        for question in questions:
            print(f"{question[0]}\nmale  \ female")
            answer_1 = input().lower()
            if not validate_data(answer_1):
                break
            print(f"{question[1]}\nweekly  \ twice a month  \ once in a while")
            answer_2 = input().lower()
            if not validate_data(answer_2):
                break
            print(f"{question[2]}\ncomputer  \ video console  \ both alike")
            answer_3 = input().lower()
            if not validate_data(answer_3):
                break   
            print(f"{question[3]}\ntrategy  \ shooting  \ sports")
            answer_4 = input().lower()
            if validate_data(answer_4):
                print("Perfect, that's it!\n")
                time.sleep(1)                
                print("LET THE BATTLE BEGIN")
                return user_answers
            else:
                validate_data(answer_4)
                break

        
def validate_data(answer):

    choises = ["male", "female", "weekly", "twice a month", " once in a while", "computer", "video console", "both alike", "strategy", "shooting", "sports"]
    try:
        if answer not in choises:
            user_answers.clear()
            raise ValueError(
                "sorry! you must select one of the given options.\n")
        user_answers.append(answer)
            
    except ValueError as e:
        print(f"Invalid answer {e}Please try again.")
        return False

    return True


def add_survey_data_worksheet(user_answers, worksheet):
    
    data_worksheet = SHEET.worksheet(worksheet)
    new_data = data_worksheet.append_row(user_answers)


def get_data_gender_worksheet(worksheet):

    data_gender = worksheet.col_values(1)
    male_gender = data_gender.count("male")
    female_gender = data_gender.count("female")
    # people = len(gender) - 1
    print(f"male: {male_gender}, female: {female_gender}")


def get_data_disponibility_worksheet(worksheet):

    data_disponibility = worksheet.col_values(2)
    weekly = data_disponibility.count("weekly")
    twice_week = data_disponibility.count("twice a week")
    once_in_while = data_disponibility.count("once in a while")
    print(F"weekly: {weekly}, twice a week: {twice_week}, once in a while: {once_in_while}")

    
def main():

    data_worksheet = SHEET.worksheet("survey")
    # user_answers = get_answers_survey()
    # add_survey_data_worksheet(user_answers, "survey")
    get_data_gender_worksheet(data_worksheet)
    get_data_disponibility_worksheet(data_worksheet)



# start_survey()
main()
# class Question
#     def __init__(self, question, a ,b , c):
#         self.question = question
#         self.a = a 
#         self.b = b 
#         self.c = c

# question_1 = Question()

