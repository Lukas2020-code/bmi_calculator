import re
from email_validator import validate_email, EmailNotValidError


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
    if not input_weight:
        raise ValueError("Weight input cannot be empty")
    if input_weight <= 0:
        raise ValueError(f"Invalid weight value. "
                         f"Weight should be a digit greater than 0")


def validate_height(input_height):
    """
    Validate the user's height to calculate BMI
    """
    if not input_height:
        raise ValueError("Height input cannot be empty")
    if input_height <= 0:
        raise ValueError(f"Invalid height value. "
                         f"Height should be a digit greater than 0")


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
            print(dob)

            break

        except ValueError as e:
            print(f'Oops, something wnet wrong! '
                  f'\nValidation error: {e}. '
                  f'\nTry again...\n')

    return name, email, gender, weight, height, dob


user_input()