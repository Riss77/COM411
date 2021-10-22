

number_cables = int(input("How many cables must I avoid?"))

count = 0

while count < number_cables:
    print("\nAvoiding...")
    print(f"...Done! {count+1} live cables avoided.")
    count += 1

print("\nAll live cables have been avoided.")