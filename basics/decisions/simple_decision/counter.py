
odds = 0
evens = 0

print("\n Please enter your first whole number\n")

first_number = int(input())

if first_number % 2 != 1:
    evens += 1
else:
    odds += 1


print("\n Please enter your second whole number\n")

second_number = int(input())

if second_number % 2 != 1:
    evens += 1
else:
    odds += 1

print("\n Please enter your third whole number\n")

third_number = int(input())

if third_number % 2 != 1:
    evens += 1
else:
    odds += 1

print(f"There were {evens} even and {odds} odds numbers")
2
