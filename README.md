# BMI Calculator

Welcome to BMI Calculator. Simple program which help you check your BMI. Program will ask you for some information and then calculate your BMI.

The life link can be found here: [bmi-calculator](https://calculate-your-bmi-50a851f64fcf.herokuapp.com/)


## How to use it
- The program will asked question which user should answer for BMI calculation at the beginning
- After each question if the answer will not be valid, user get information on the screen
- When all the information provided by user will be valid the program will calculate the BMI
- The result will be displayed on the screen for the user with a short message

## Site owner goal
- Provide a user with simple BMI calculator
- 
## Features

### Existing Features
- Calculate User Age
    - This function calculate user age to store it in the workseet

 - Calculate BMI
    - User provide the weight and height
    - This function calculate user BMI by provided data

  - Display result to the user
    - User get a calculated result of BMI
    - It also get a short message from the program acording to the BMI result

   - Updating the API
    - Store the user information in Google Sheets

 ### Features to Improve

## Data Model
First the program collect the inforation from the user if all of thenm will get through the vakidation process

Then some of the information are used in other task to complete the program requirements.



## Testing
- The project was tested manually by me, my familly and closes friends.
- Tests for all inputs and check the validation e.g.:
     - numbers in user name
     - email without @ sign
     - used any other number or letter which are not F or M
     - give a char or string in weight or height
     - write a date of birth which is not if format dd/mm/yyyy, e.g. used - instead
- Tested in my terminal on PyCharm, the codeanywhere terminal when writting the project and on Heroku terminal.
- 

### Bugs

#### Solved Bugs
- When calculating the user age I found out that the first approach which I have doesn't calculate the months and days correctly e.g. when user birthday was the next day of today it was still counted like the user is already a plus year old. It goes by the year, not includind the months and days. The second solution which I found online sole the problem. I credited the source below in Credit section.
- I decided to use external python library email_validator instead of regex for email validation. It's designed for this purpose and shorter to write than regex expesion which sometimes didn't catch the wrong email.

### Validator Testing
- PEP8
    - Passed the PEP8 validation with no errors found.

## Deploy
The application is deployed on Heroku platform (which is used for backend project) using Code Institute mock terminal.
To achive that the following steps have to be taken
 - Copy the repository
 - Create a Heroku Application


## Credits
all the credit in the application goes here
