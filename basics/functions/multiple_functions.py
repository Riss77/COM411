def display_ladder(steps):
    for step in range(steps):
        print("| |")
        print("***")

    print("| |")


def create_ladder():
    steps = int(input("How many steps remain?\n"))
    display_ladder(steps)

create_ladder()