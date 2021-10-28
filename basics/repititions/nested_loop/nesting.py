
sequence = input("Please enter a sequence\n")


marker = input("Please enter the character for the marker\n")

marker1 = -1

marker2 = -1

for position in range (0, len(sequence), 1):
    letter = sequence[position]

    if letter == marker:
        if marker1 == -1:
            marker1 = position
        else:
            marker2 = position

print(f"The distance between the markers is {marker2 - marker1 -1}.")

