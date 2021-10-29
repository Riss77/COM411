# define function named directions

def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


# define function named run

def run():
    print(directions())


# call function (code ensures is only called when executed directly

if __name__ == "__main__":
    run()
