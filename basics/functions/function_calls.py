def display(word):
    num_dashes = 2 + len(word)
    print("-" * (num_dashes + 1))
    print(f"| {word} |")
    print("-" * (num_dashes + 1))


def lower_case(word):
    print(word.lower())


def upper_case(word):
    print(word.upper())


def mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word}| {mirrored}")


def repeat(word):
    number = int(input("Please enter the number of times to display the word\n"))

    for number in range(number):
        if number % 2 == 0:
            print(word.lower())
        else:
            print(word.upper())


def run():
    word = input("Please enter a word:\n")

    print("Please chose an action for this word")
    print("[1] Display in a box")
    print("[2] Display lower-case")
    print("[3] Display upper-case")
    print("[4] Display mirrored")
    print("[5] Display repeated")
    print("[6] Quit")

    method = int(input())

    if method == 1:
        display(word)
    elif method == 2:
        lower_case(word)
    elif method == 3:
        upper_case(word)
    elif method == 4:
        mirrored(word)
    elif method == 5:
        repeat(word)
    else:
        print("You have chosen to end the program.")

run()

