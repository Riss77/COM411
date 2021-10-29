def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run():
    probability = likelihood()
    print(f"Minimum likelihood of falling: {probability[0]}%")
    print(f"Maximum likelihood of falling: {probability[1]}%")


if __name__ == "__main__":
    run()
