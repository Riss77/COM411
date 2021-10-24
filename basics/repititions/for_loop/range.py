

level_req = int(input("What level of brightness is required?\n"))

print("Adjusting brightness...\n")

for brightness in range(0, level_req+1, 2):
    print(f"Beep's brightness level:{'*' * brightness}")
    print(f"Bop's brightness level:{'*' * brightness}")

print("Adjustments complete!\n")
