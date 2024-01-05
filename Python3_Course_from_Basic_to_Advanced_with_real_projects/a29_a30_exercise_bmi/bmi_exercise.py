"""
- Create variables for name (str), age (int), height (float) and
weight (float) of a person;
- Create variables with the current year (int);
- Get the person's year of birth (based on age and current year);
- Obtain the person's BMI to 2 decimal places (the person's weight and height);
- Display text with all values on the screen using F-strings (with keys).
"""
from datetime import datetime

name = str(input('Type your name: ')).capitalize()
age = int(input('Type your age: '))
height = float(input('Type your height in meters: '))
weight = float(input('Enter your weight: '))
actual_year = datetime.now().year
birth_date = actual_year - age
bmi = weight / (height ** 2)

print(f'{name} has {age} years old, {height:.2f}m of height and your weight is {weight} Kg.')
print(f'The BMI of {name} is {bmi:.2f}.')
print(f'{name} was born in {birth_date}.')
