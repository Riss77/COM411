import matplotlib.pyplot as plt
import csv


def read_data():
    data = {'survived': [], 'sex': [], 'age': [], 'fare': []}

    with open('titanic.csv') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

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
    children = {'survived': [], 'deceased': []}
    adults = {'survived': [], 'deceased': []}
    elderly = {'survived': [], 'deceased': []}

    for index in range(len(data['age'])):
        age = data['age'][index]
        if age < 18 and data['survived'][index]:
            children['survived'].append(age)
        elif age < 18 and not data['survived'][index]:
            children['deceased'].append(age)
        elif age < 65 and data['survived'][index]:
            adults['survived'].append(age)
        elif age < 65 and not data['survived'][index]:
            adults['deceased'].append(age)
        elif data['survived'][index]:
            elderly['survived'].append(age)
        else:
            elderly['deceased'].append(age)

    labels = ['Children', 'Adults', 'Elderly']
    survivors = [len(children['survived']), len(adults['survived']), len(elderly['survived'])]
    deceased = [len(children['deceased']), len(adults['deceased']), len(elderly['deceased'])]

    axs.bar(labels, survivors, label='Survived')
    axs.bar(labels, deceased, bottom=survivors, label='Deceased')
    axs.set_ylabel('Age')
    axs.legend()
    axs.set_title('Age vs Survival')


def plot_age_vs_fare_scatter(axs, data):
    #age = data['age']
    #fare = data['fare']

    #axs.scatter(age, fare, 'o')
    #axs.set_ylabel('Fare')
    #axs.set_xlabel('Age')
    #axs.legend()
    #axs.set_title('Fare vs Age')
    pass


def plot_survived_vs_sex_bar(axs, data):
    male = {'survived': [], 'deceased': []}
    female = {'survived': [], 'deceased': []}

    pass


def plot_fare_vs_survived(axs, data):
    survived = []
    deceased = []

    pass


def run():
    data = read_data()
    fig, axs = plt.subplots(2, 2)
    plot_survivor_age_bar(axs[0, 0], data)
    plot_age_vs_fare_scatter(axs[0, 1], data)
    plot_survived_vs_sex_bar(axs[1, 0], data)
    plot_fare_vs_survived(axs[1, 1], data)

    plt.tight_layout()
    plt.show()
    print(f"survived:{len(data['survived'])}, sex:{len(data['sex'])}, age:{len(data['age'])}, fare:{len(data['fare'])}")


run()

