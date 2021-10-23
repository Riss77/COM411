
user_number = int(input("Please enter a number:"))

iteration = 0
fact_number = 1

while user_number > 0:
    fact_number = fact_number * user_number
    user_number -= 1

print(f"The factorial is {fact_number}")