def started(msg=""):
    print("-"*85)
    print(f"Operation started: {msg}\n...")


def completed():
    print("\nOperation completed.")
    print("-"*85)


def err(msg):
    print(f"Error! {msg}")


def menu():
    print(
        """
        Please select one of the following options:
        [years]    List unique years
        [tally]    Tally up medals
        [team]   Tally up medals for each team
        [exit]     Exit the program
        """)
    chosen_option = input("Your selection:")
    return chosen_option


def display_medal_tally(tally):
    print(f"| Gold       | {tally['Gold']}      |")
    print(f"| Silver     | {tally['Silver']}     |")
    print(f"| Bronze     | {tally['Bronze']}      |")


def display_team_medal_tally(team_tally):
    for key, value in team_tally.items():
        print(f"{key}")
        print(f"Gold: {value['Gold']}, Silver: {value['Silver']}, Bronze: {value['Bronze']}")


def display_years(years):
    for data in sorted(years):
        print(f"{data}")
