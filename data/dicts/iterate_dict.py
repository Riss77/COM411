def pattern():
    data = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return data


def display_keys(data):
    print("Keys:")
    for key in data.keys():
        print(key)


def display_values(data):
    print("Values:")
    for value in data.values():
        print(value)


def display_items(data):
    print("Pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")


def run():
    data = pattern()
    print(f"Dictionary: \n{data}")

    display_keys(data)
    display_values(data)
    display_items(data)


run()
