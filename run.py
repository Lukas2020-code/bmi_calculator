# function to get user input
def user_input():
    print("Please provide some information which helps calculate your BMI")

    while True:
        try:
            name = input("Please type your name:\n")
            print(name)

            email = input("Please write your email:\n")
            print(email)

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
            print(f'Oops, something wnet wrong! Validation error: {e}. Try again...')

    return name, email, gender, weight, height, dob        