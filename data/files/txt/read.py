def display_chars(file_path, num_char):
    with open(file_path) as file:
        data = file.read(num_char)
        print(f"The first {num_char} characters are:")
        print(data)
        print("\n")


def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print("The first line is:")
        print(data)
        print("\n")


def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print("The full text is:")
        print(data)
        print("\n")


def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()
