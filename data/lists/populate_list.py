def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("\nPlease select a direction:")
    user_direction = directions()
    for index in range(len(user_direction)):
        print(f"{index}:{user_direction[index]}")
    index = int(input())
    return user_direction[index]


def run():
    route = []
    print("Working out escape route...")
    for count in range(5):
        route.append(menu())
    print(f"Escape route: {route}")


if __name__ == "__main__":
    run()