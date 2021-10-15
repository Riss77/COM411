# define and obtain name variable
name = input("What is your name human?\n")
# define and obtain age variable as an integer
age = int(input("How old are you (in years)?\n"))
# define and obtain height variable as a float
height = float(input("How tall are you (in meters)?\n"))
# define and obtain weight variable as a float
weight = float(input("How much do you weigh (in kilograms)?\n"))
# Calculation for bmi (weight divided by height squared)
bmi = weight / (height**2)
formatted_bmi = "{:.2f}".format(bmi)
# print line with the variables and calculated variable
print(f"{name} you are {age} years old and your bmi is {formatted_bmi}.")
