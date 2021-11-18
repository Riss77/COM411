import matplotlib.pyplot as plt
import random as rnd


def data():
    paths = {}
    print("What type of line would you like? (:, -- or -)\n")
    type_line = input()
    print("What colour would you like? (r, g or b)")
    colour = input()
    print("What style of marker would you like? (o, s or ^)")
    marker = input()

    paths['type_line'] = type_line
    paths['colour'] = colour
    paths['marker'] = marker

    return paths


def generate():
    print("How many lines would you like to display?")
    num_lines = int(input())

    for num_line in range(num_lines):
        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        format2 = f"{values['colour']}{values['type_line']}{values['marker']}"
        plt.plot(x, y, format2)

    plt.show()


def run():
    print("Running...")
    generate()
    print("Done!")


run()
