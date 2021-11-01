def sum_weights(weight1, weight2):
    total_weight = weight1 + weight2
    return total_weight


def calc_avg_weight(weight1, weight2):
    avg_weight = sum_weights(weight1, weight2) / 2
    return avg_weight


def run():
    weight1 = float(input("Please enter the weight of Beep:\n"))
    weight2 = float(input("Please enter the weight of Bop:\n"))
    method = input("Please enter 'sum' for a total or 'average' for the weights\n")
    if method == "sum":
        answer = sum_weights(weight1, weight2)
        print(f"The sum of Beep's and Bop's weight is {answer:.2f}")
    elif method == "average":
        answer = calc_avg_weight(weight1, weight2)
        print(f"The average of Beep's and Bop's weight is {answer:.2f}")
    else:
        print("I'm sorry that is not recognised.")


if __name__ == "__main__":
    run()
