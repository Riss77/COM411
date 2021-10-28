

phrase = input("What phrase do you see?\n")

print("\nReversing...")
print("The phrase is ", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)

