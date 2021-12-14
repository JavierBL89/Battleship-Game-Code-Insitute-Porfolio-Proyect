import random
import time
import math
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
    """ 
    Inside the try clear the user's answers list and
    raises an error if incorrect data entered
    """
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
    """
    Access the survey worksheet
    Append the user's data into the worksheet
    """
    data_worksheet = SHEET.worksheet(worksheet)
    new_data = data_worksheet.append_row(user_answers)


def get_data_gender_worksheet(worksheet):
    """"
    Get user's gender data from worksheet
    Calculate data percetages
    """
    data_gender = worksheet.col_values(1)
    male_data = data_gender.count("male")
    female_data = data_gender.count("female")
    people = len(data_gender) - 1
    # print(f"male: {male_gender}, female: {female_gender}")
    total_male = round(int((male_data / people) * 100))
    total_female = round(int((female_data / people) * 100))
    print(f"male: {total_male}%, female: {total_female}%")
    return total_male, total_female 


def get_data_availability_worksheet(worksheet):
    """ 
    Get data user's availability to play video games from worksheet
    Calculate data percentages
    """
    data_availability = worksheet.col_values(2)
    weekly = data_availability.count("weekly")
    twice_week = data_availability.count("twice a week")
    once_in_while = data_availability.count("once in a while")
    people = len(data_availability) - 1

    total_weekly = round((weekly / people) * 100)
    total_twice_a_week = round((twice_week / people) * 100)
    total_once_in_while = math.floor((once_in_while / people) * 100 )
    print(F"weekly: {total_weekly}%, twice a week: {total_twice_a_week}%, once in a while: {total_once_in_while}%")
    return total_weekly, total_twice_a_week, total_once_in_while


def get_data_devices_worksheet(worksheet):
    """"
    Get data user's prefered devices from worksheet
    Calculate data percentages
    """
    data_devices = worksheet.col_values(3)
    computer = data_devices.count("computer")
    video_console = data_devices.count("video console")
    both_devices = data_devices.count("both alike")
    people = len(data_devices) - 1

    total_computer = round((computer / people) * 100)
    total_video_console = round((video_console / people) * 100)
    total_both_devices = math.floor((both_devices / people) * 100)
    print(F"computer: {total_computer}%, video console: {total_video_console}%, both devices: {total_both_devices}%")
    return total_computer, total_video_console, total_both_devices


def get_data_game_plot(worksheet):
    """"
    Get data user's prefered kind of game from worksheet
    Calculate data percentages
    """
    data_game_plot = worksheet.col_values(4)
    strategy = data_game_plot.count("strategy")
    shooting = data_game_plot.count("shooting")
    sports = data_game_plot.count("sports")
    people = len(data_game_plot) - 1

    total_strategy = round((strategy / people) * 100)
    total_shooting = round((shooting / people) * 100)
    total_sports = math.floor((sports / people) * 100)
    print(f"strategy: {total_strategy}%, shooting: {total_shooting}%, sports: {total_sports}%\n")
    return total_strategy, total_shooting, total_sports


def main():

    data_worksheet = SHEET.worksheet("survey")
    # user_answers = get_answers_survey()
    # add_survey_data_worksheet(user_answers, "survey")
    data_gender = get_data_gender_worksheet(data_worksheet)
    data_availability = get_data_availability_worksheet(data_worksheet)
    data_devices = get_data_devices_worksheet(data_worksheet)
    data_game_plot = get_data_game_plot(data_worksheet)
    # calculate_data = calculate_data_survey(data_gender, data_availability, data_devices, data_game_plot)

# start_survey()
main()
# class Question
#     def __init__(self, question, a ,b , c):
#         self.question = question
#         self.a = a 
#         self.b = b 
#         self.c = c

# question_1 = Question()

