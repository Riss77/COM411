
amount_numbers = int(input("How many numbers should I sum up?\n"))

sum_numbers = 0
count = 0

while count < amount_numbers:
    current_number = int(input(f"Please enter a number 1 of {amount_numbers}\n"))
    sum_numbers = sum_numbers + current_number
    count += 1

print(f"The answer is {sum_numbers}\n")