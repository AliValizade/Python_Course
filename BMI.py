weight = float(input("Plz enter your weight in kilogram: "))
height = float(input("Plz enter your height in meter : "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("you are underweight!")
elif 24.9 > bmi >= 18.5 :
    print("You are Normal.")
elif 29.9 > bmi > 25:
    print("You are Overweight!")
elif 34.9 > bmi > 30:
    print("You are Obese.")
elif bmi > 35:
    print("You are Extremely Obese.")