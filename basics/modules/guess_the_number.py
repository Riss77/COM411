import random

min_val = int(input("Please enter the minimum value:\n"))
max_val = int(input("Please enter the maximum value:\n"))

value = random.randrange(min_val, max_val)
print(f"I am thinking of a number between {min_val} and {max_val}.\n Can you guess what it is?\n")

while True:
    guess = int(input("Please enter a number:\n"))

    if guess == value:
        print("You guessed correctly!")
        break
    elif guess < value:
        print("Your guess is too low, please try again.\n")
    else:
        print("Your guess is too high, please try again.\n")

print("Game Over!")