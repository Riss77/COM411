
user_string = str()

print("What strange markings do you see?")

user_word = input()

print("Identifying...")

for count in range(0, len(user_word), 1):
    print(f"index {count}:", user_word[count])

print("Done!\n")
