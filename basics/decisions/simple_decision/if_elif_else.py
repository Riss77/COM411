# ask user for directional input
print("\nTowards which direction should I paint (up, down, left or right?)\n")

direction = input()
# if statement for up
if direction == "up":
    print("\nI am painting in the upward direction!\n")

elif direction == "down":
    print("\nI am painting in the downward direction!\n")

elif direction == "left":
    print("\nI am painting in the leftward direction!\n")

elif direction == "right":
    print("\nI am painting in the rightward direction!\n")
else:
    print("\nI do not know what I am doing!\n")