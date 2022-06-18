print('*'*50)
height = float(input('enter your height in inches:\t'))
weight = float(input('enter your weight in lbs:\t'))
bmi = round((weight * 703) / (height**2), 1)

if bmi < 16.0:
    result = 'Severely Underweight'
elif bmi > 16.0 and bmi < 18.4:
    result = 'Underweight'
elif bmi > 18.5 and bmi < 24.9:
    result = 'Normal'
elif bmi > 25.0 and bmi < 29.9:
    result = 'Overweight'
elif bmi > 30.0 and bmi < 34.9:
    result = 'Moderately Obese'
elif bmi > 35.0 and bmi < 39.9:
    result = 'Severely Obese'
elif bmi > 39.9:
    result = 'Morbidly Obese'
else:
    result = 'IDK'


print(f'Your BMI of {bmi} makes you {result}')
