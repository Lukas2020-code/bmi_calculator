import re
from email_validator import validate_email, EmailNotValidError
from datetime import datetime


def has_numbers(name):
    """
    Check if user's name contains any digit
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
    """
    if not input_name:
        raise ValueError("Name cannot be empty!")
    if len(input_name) < 2:
        raise ValueError("Name cannot be shorter than two chars")
# references for re.match in python
# https: // www.w3schools.com / python / python_regex.asp
# https://docs.python.org/3/library/re.html
    if not re.match(r"^[A-Za-z\s]+$", input_name) and input_name.strip():
        raise ValueError("Invalid name format. Please use e.g.: Joe Doe")
    if has_numbers(input_name):
        raise ValueError("Please don't write numbers in your name!")


def valid_email(input_email):
    """
    Validate user's email address
    using email_validator external library
    """
    if not input_email:
        raise ValueError("Email Address input cannot be empty.")
    if not validate_email(input_email):
        raise EmailNotValidError


def validate_gender(input_gender):
    """
    Validate user's gender
    """
    if not input_gender:
        raise ValueError("Gender input cannot be empty.")
    if input_gender not in ['F', 'M']:
        message = "Please choose between: F - Female / M - Male."
        raise ValueError("Invalid gender provided. " + message)


def validate_weight(input_weight):
    """
    Validate the user's weight to calculate BMI
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
    Get user inputs
    """
    print("\nPlease provide some information which helps calculate your BMI")

    while True:
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
            print(f'Oops, something wnet wrong! '
                  f'\nValidation error: {e}. '
                  f'\nTry again...\n')

    return name, email, gender, weight, height, dob


# function to calculate user age
def calculate_user_age(dob):
    """
    This function calculate user's age
    """
    # Change the dob string into date object
    dob_date = datetime.strptime(dob, "%d/%m/%Y")
    # Take the current time
    current_date = datetime.now()
    # calculate the age
    age = current_date.year - dob_date.year
    # check if day or month passed the date of birth
    if current_date.month < dob_date.month or (current_date.month == dob_date.month and current_date.day < dob_date.day):

        age += 1

    return age


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


user_input()