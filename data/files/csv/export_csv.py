import csv


def export(file_path, num_bots):
    print("Exporting...")
    with open(file_path, "a") as file:
        for count in range(num_bots):
            bot_id = int(input("Please enter the bot id:\n"))
            bot_name = input("Please enter the bot name:\n")
            bot_paint = input("Please enter the bot paint colour:\n")
            data = f"{bot_id},{bot_name},{bot_paint}\n"
            file.write(data)
    print("Done!")


def run():
    export("exported_bots.csv", 2)


if __name__ == "__main__":
    run()
