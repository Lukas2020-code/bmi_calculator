import re
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
from PIL import Image


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


def bmi_result(result, email):
    """
    That function will display the result of user's BMI calculation
    and tell the user in which range he/she is. It will also send an email
    with some tips and advice if BMI is not in normal range.
    """
    if result < 18.5:
        print(f'Your bmi result is: {result}')
        print(f'It looks like your are in underweight range. '
              f'On email address {email} we send you some tips and advise '
              f'to improve your BMI.')
    elif 18.5 < result < 24.9:
        print(f'Your bmi result is: {result}')
        print(f'Your Healthy. You have nothing to worry about. '
              f'Keep up good work!')
    elif 29.9 < result < 25.0:
        print(f'Your bmi result is: {result}')
        print(f'It looks like your are in overweight range. '
              f'On email address {email} we send you some tips and advise '
              f'to improve your BMI.')
    else:
        print(f'Your bmi result is: {result}')
        print(
            f'It looks like your are in obese range. '
            f'On email address {email} we send you some tips and advise '
            f'to improve your BMI.')


# references: 
# https://www.geeksforgeeks.org/display-images-on-terminal-using-python/
def upload_image():
    """
    This function will load and display the BMI table for the user's.
    It should help them visualize where they are with their BMI calculations.
    I used outside library to achive the image to load
    """
    # create an AnsiImage instance from an image file
    image = Image.open("assets/images/bmi_table.png")
    # display the image in console
    image.show()         


def main():
    """
    Main function will run whole programm. It will take user input, 
    then calculate BMI, show result to the user and exit the program.
    """
    print("\nWelcome to BMI Calculator")
    print(f'\nIt will help you calculate your BMI '
          f'and compare your result with the graph')
    # unpack each user input into variable
    name, email, gender, weight, height, dob = user_input()

    # checking the user input for gender
    if gender == 'F':
        gender_str = 'Female'
    elif gender == 'M':
        gender_str = 'Male'

    # calculate the user age
    age = calculate_user_age(dob)

    # checking age cause BMI should not be done for people under 2 years
    if age <= 2:
        print("Sorry you are to young for BMI test calculation. Good Bye!")
        return

    print(f'\nYour name is: {name}')
    print(f'You are a {gender_str} and your age is {age}')

    if age > 2:
        # calculate the user bmi
        bmi = bmi_calculator(weight, height)
        # display the user bmi result
        bmi_result(bmi, email)
        print(f'You can compare your result on the BMI chart '
              f'which open in new window')
        # display the bmi table image
        upload_image() 

    print("\nThank you for using BMI calculator. All the best!!!")


main()    