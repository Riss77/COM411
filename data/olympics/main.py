import csv
import process
import tui

records = []
headings = []


def read_data(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader)
        print(f"Headings:\n{headings}")

        print("Values:")
        for values in csv_reader:
            print(values)


def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            pass
        elif selection == "tally":
            pass
        elif selection == "team":
            pass
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()
