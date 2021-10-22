

type_adventure = input("What type of adventure would you like to go on?")

if (type_adventure == "scary") or (type_adventure == "short"):
    print("Entering the dark forest!")
elif (type_adventure == "safe") or (type_adventure == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")