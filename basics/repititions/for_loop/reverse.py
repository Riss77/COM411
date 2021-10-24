

phrase = input("What phrase do you see?\n")

print("\nReversing...")
print("The phrase is ", end="")

for count in range(len(phrase) - 1, -1, -1):
    print(phrase[count], end="")
