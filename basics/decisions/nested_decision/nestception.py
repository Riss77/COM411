place = input("Where should I look?")

if place == "in the bedroom":
    bedroom = input("Where in the bedroom should I look?")
    if bedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")

if place == "in the bathroom":
    bathroom = input("Where in the bathroom should I look?")
    if bathroom == "in the bathtub":
        print("Found a rubber ducky but no battery")
    else:
        print("Found a wet surface but no battery")
else:
    print("I do not know here that is but I will keep looking")
