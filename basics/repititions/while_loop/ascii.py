
bars = int(input("How many bars should be charged?\n"))

charged_bars = 0

while charged_bars < bars:
    print(f"Charging: {'█ ' * (charged_bars + 1)}")
    charged_bars += 1

print("\nThe battery is fully charged.")

