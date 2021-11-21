import matplotlib.pyplot as plt
import csv


def read_data():
    with open('titanic.csv') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        data = {'survived': [], 'sex': [], 'age': [], 'fare': []}

        for line in csv_reader:
            survived = line[1].strip()
            sex = line[14].strip()
            age = line[4].strip()
            fare = line[8].strip()

        if survived != "" and sex != "" and age != "" and fare != "":
            data['survived'].append(bool(int(survived)))

            if int(sex) == 0:
                data['sex'].append('male')
            else:
                data['sex'].append('female')

            data['age'].append(float(age))
            data['fare'].append(round(float(fare), 2))
    return data


def plot_survivor_age_bar(axs, data):
    children = 0
    adults = 0
    elderly = 0

    for line in csv:
        if line[4] != "" and line[1] == 1:
            age = float(line[4])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1

    x = ['Children', 'Adults', 'Elderly']
    y = [{children}, {adults}, {elderly}]
    plt.xlabel("Age Group")
    plt.ylabel("Total Survivors")
    plt.bar(x, y)


def plot_age_vs_fare_scatter(axs, data):
    for line in csv:
        if line[4] != "" and line[8] != "":
            age = float(line[4])
            fare = float(line[8])

    plt.xlabel("Age")
    plt.ylabel("Fare")

    plt.scatter(age, fare, "o")


def plot_survived_vs_sex_bar(axs, data):
    pass


def run():
    data = read_data()
    #fig, axs = plt.subplots(2, 2)
    #plot_survivor_age_bar(axs[0, 0], data)
    #plot_age_vs_fare_scatter(axs[0, 1], data)
    #plot_survived_vs_sex_bar(axs[1, 0], data)
    #(axs[1, 1], data)

    #plt.tight_layout()
    #plt.show()
    print(f"{data}")


run()

