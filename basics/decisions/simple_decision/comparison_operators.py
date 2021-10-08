
print("\n Please enter your first number\n")

first_number = int(input())

print("\n Please enter your second number\n")

second_number = int(input())

if first_number < second_number:
    print("The first number is smallest.")
elif first_number > second_number:
    print("The second number is smallest.")
else:
    print("Both are are equal.")