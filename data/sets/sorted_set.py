def observed():
    observations = []

    for count in range(5):
        print("Please enter an observation:")
        observations.append(input())

    return observations


def remove_observations(observations):
    answer = input("Do you wish to remove any observations?\n")
    if answer == "yes":
        to_be_removed = input("Which sight would you like removed?\n")
        observation = input()
        observations.remove(observation)
    else:
        print("No values to be removed.\n")


def run():
    print("Counting observations...")
    observations = observed()
    remove_observations(observations)
    observations_set = set()

    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    for data in sorted(observations_set):
        print(f"{data[0]} observed {data[1]} times.")


run()

