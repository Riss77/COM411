

print("\nProgram Started!\n")

character = input("Please enter a standard character:\n")

if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}\n")
else:
    print("A single character should be chosen\n")
print("Program Ended!")
