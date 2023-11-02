import re
from email_validator import validate_email, EmailNotValidError


def has_numbers(name):
    """
    Check if user name contains any digit
    """
    # for char in name:
    #     if char.isdigit():
    #         return True
    # return False
    return any(char.isdigit() for char in name)


# create a function to validate user name
def validate_name(input_name):
    """
    Validate user name using regex and has_number method
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
    Validate user email address 
    using email_validator external library
    """  
    if not input_email:
        raise ValueError("Email Address input cannot be empty.")
    if not validate_email(input_email):
        raise EmailNotValidError


# function to get user input
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
            print(gender)

            weight = float(input("Please type your weight in kg:\n"))
            print(weight)

            height = float(input("Please provide your height in cm:\n"))
            print(height)

            dob = input("Enter you date of birth in format dd/mm/yyyy:\n")
            print(dob)

            break

        except ValueError as e:
            print(f'Oops, something wnet wrong! '
                  f'Validation error: {e}. '
                  f'Try again...')

    return name, email, gender, weight, height, dob
    

user_input()