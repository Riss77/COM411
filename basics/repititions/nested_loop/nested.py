

rows = int(input("How many rows should I have?\n"))

columns = int(input("how many columns should I have?\n"))

for row in range (0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
    print()
