import re
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
from PIL import Image
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('calculate_user_bmi')

users = SHEET.worksheet('users')


def has_numbers(name):
    """
    method to check if user's name contains any digit
    """
    # for char in name:
    #     if char.isdigit():
    #         return True
    # return False
    return any(char.isdigit() for char in name)


# create a function to validate user name
def validate_name(input_name):
    """
    Validate user's name using regex and has_number method
    This method should tell if user name have only letters,
    is not empty, match the given pattern and is longer than 2 chars.
    """
    if not input_name:
        raise ValueError("Name cannot be empty!")
    if len(input_name) < 2:
        raise ValueError("Name cannot be shorter than two chars")
# references for re.match in python
# https: // www.w3schools.com / python / python_regex.asp
# https://docs.python.org/3/library/re.html
    if not re.match(r"^[A-Za-z\s]+$", input_name) and input_name.strip():
        raise ValueError("Invalid name format. Please type e.g.: Joe Doe")
    if has_numbers(input_name):
        raise ValueError("Please don't write numbers in your name!")


def valid_email(input_email):
    """
    Validate user's email address
    using email_validator external library.
    """
    if not input_email:
        raise ValueError("Email Address input cannot be empty.")
    if not validate_email(input_email):
        raise EmailNotValidError


def validate_gender(input_gender):
    """
    Validate user gender
    """
    if not input_gender:
        raise ValueError("Gender input cannot be empty.")
    if input_gender not in ['F', 'M']:
        message = "Please choose between: F - Female / M - Male."
        raise ValueError("Invalid gender provided. " + message)


def validate_weight(input_weight):
    """
    Validate the user's weight to calculate BMI
    Height have to greater than 0 and should be a digit
    """
    if input_weight <= 0:
        raise ValueError(f"Invalid weight value. "
                         f"Weight should be a digit greater than 0")


def validate_height(input_height):
    """
    Validate the user's height to calculate BMI
    """
    if input_height <= 0:
        raise ValueError(f"Invalid height value. "
                         f"Height should be a digit greater than 0")


# references https://www.geeksforgeeks.org/python-validate-string-date-format/
def validate_dob(input_dob):
    if not input_dob:
        raise ValueError("Date of birth cannot be empty.")
    date_format = r'^\d{2}/\d{2}/\d{4}$'
    if not re.match(date_format, input_dob):
        raise ValueError(f"Invalid date format! "
                         f"Please provide date in format dd/mm/yyyy.")


def user_input():
    """
    Get user's inputs for our program.
    User provide some information until all will be valid.
    Then the program will move on.
    """
    # print("\nPlease provide some information which helps calculate your BMI")

    while True:
        print("Please provide some information to calculate your BMI")
        try:
            name = input("Please type your name:\n")
            validate_name(name)

            email = input("Please write your email:\n")
            valid_email(email)

            gender = input("Please type your gender (F/M):\n")
            validate_gender(gender)

            weight = float(input("Please type in your weight in kg:\n"))
            validate_weight(weight)

            height = float(input("Please type in your height in cm:\n"))
            validate_height(height)

            dob = input("Enter your date of birth in format dd/mm/yyyy:\n")
            validate_dob(dob)

            break

        except ValueError as e:
            print(f'Oops, something wnet wrong!\n'
                  f'Validation error: {e}.\n'
                  f'Try again...\n')

    return name, email, gender, weight, height, dob


# function to calculate user age
def calculate_user_age(dob):
    """
    This function calculate user's age
    """
    # seperate the dob date into single strings
    user_date = dob.split("/")

    # cast those strings into ints
    day = int(user_date[0])
    month = int(user_date[1])
    year = int(user_date[2])

    today = datetime.now()
    # calculate user age
    user_age = today.year - year - ((today.month, today.day) < (month, day))

    return user_age


def bmi_calculator(user_weight, user_height):
    """
    This function calculates the user's BMI
    """
    # converts the height from cm into metres
    height = user_height / 100
    # calculate the bmi for metric units
    result = user_weight / (height * height)
    # round the result to two decimal places
    rounded_result = round(result, 2)

    return rounded_result


def bmi_result(result, email):
    """
    That function will display the result of user's BMI calculation
    and tell the user in which range he/she is. It will also send an email
    with some tips and advice if BMI is not in normal range.
    """
    if result < 18.5:
        print(f'\nYour bmi result is: {result}')
        print(f'It looks like your are in underweight range. '
              f'On email address {email} we send you some tips and advise '
              f'to improve your BMI.')
    elif 18.5 < result < 24.9:
        print(f'\nYour bmi result is: {result}')
        print(f'Your Healthy. You have nothing to worry about. '
              f'Keep up good work!')
    elif 29.9 < result < 25.0:
        print(f'\nYour bmi result is: {result}')
        print(f'It looks like your are in overweight range. '
              f'On email address {email} we send you some tips and advise '
              f'to improve your BMI.')
    else:
        print(f'\nYour bmi result is: {result}')
        print(f'It looks like your are in obese range. '
              f'On email address {email} we send you some tips and advise '
              f'to improve your BMI.')


def update_users_worksheet(new_data):
    """
    Update users worksheet, add new row with the data
    """
    print(f'Your information will be store in our worksheet'
          f'if you would like to check them.\n')
    print("Updating users worksheet. Please wait...\n")
    # choose users worksheet to store the data
    users_worksheet = SHEET.worksheet('users')
    # updating the worksheet with user data
    users_worksheet.append_row(new_data)

    print("User data updated successfully.\n")


def main():
    """
    Main function run the programm. It will take user input,
    then calculate BMI, show result to the user with short informatio,
    updating users worksheet and exit the program.
    """
    print("Welcome to BMI Calculator\n")
    print(f'It will help you calculate your BMI '
          f'and compare your result with the graph\n')
    # unpack each user input into variable
    name, email, gender, weight, height, dob = user_input()

    # checking the user input for gender
    gender_str = "Female" if gender == "F" else "Male"

    # calculate the user age
    age = calculate_user_age(dob)

    # checking age cause BMI should not be done for people under 2 years
    if age <= 2:
        print("Sorry you are to young for BMI test calculation. Good Bye!\n")
        return

    print(f'\nHello {name}')
    print(f'We know that you are a {gender_str} '
          f'and your age is {age}\n')

    if age > 2:
        # calculate the user bmi
        bmi = bmi_calculator(weight, height)
        # display the user bmi result
        bmi_result(bmi, email)
        # collect all the data into list
        user_data = [name, email, gender, weight, height, dob, age, bmi]
        # update the worksheet with user data
        update_users_worksheet(user_data)

    print("Thank you for using BMI calculator. All the best!!!")


main()
