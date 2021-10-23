
print("Calculating the sum of the first 100 numbers...")

sum_numbers = 0
count = 0

while count < 100:
    sum_numbers = sum_numbers + (count+1)
    count += 1

print(f"...Done! The answer is {sum_numbers}")