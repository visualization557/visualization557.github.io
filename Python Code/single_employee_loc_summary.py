from os.path import join
from csv import reader
import matplotlib.pyplot as plt
import numpy as np

path = './assignment2/'
personal_data_dic = {}

def read_file(filename, isCredit):
    with open(join(path, filename), encoding="ISO-8859-1") as f:
        csv_reader = reader(f)
        next(csv_reader) # skip header
        for row in csv_reader:
            first = row[3]
            last = row[4]
            name = first + " " + last
            loc = row[1]
            price = row[2]
            if name in personal_data_dic:
                if loc not in personal_data_dic[name]:
                    personal_data_dic[name][loc] = [0, 0]
            else:
                personal_data_dic[name] = {}
                personal_data_dic[name][loc] = [0, 0]
            if isCredit:
                personal_data_dic[name][loc][0] += float(price)
            else:
                personal_data_dic[name][loc][1] += float(price)

def generate_personal_data_dic():
    read_file("cc_data.csv", True)
    read_file("loyalty_data.csv", False)

def get_personal_data(name):
    data = personal_data_dic[name]
    # total money spent in each location
    locations = []
    credit_amount = []
    loyalty_amount = []

    for loc, amount in data.items():
        locations.append(loc)
        credit_amount.append(amount[0])
        loyalty_amount.append(amount[1])

    # display bar chart
    fig, ax = plt.subplots(figsize=(20,12))
    ax.set_title('Money Spent by ' + name)
    x = np.arange(len(locations))
    credit = ax.bar(x - 0.15, credit_amount, label="credit", width=0.30)
    loyalty = ax.bar(x + 0.15, loyalty_amount, label="loyalty", width=0.30)
    ax.set_xticks(x)
    ax.set_xticklabels(locations, rotation=45, ha='right')
    ax.legend(loc="upper right")

    ax.bar_label(credit, padding=3, size=8)
    ax.bar_label(loyalty, padding=3, size=8)
    # plt.show()
    plt.savefig("./employee_summary/" + name + "_" + "summary.png")

generate_personal_data_dic()
for employee in personal_data_dic.keys():
    get_personal_data(employee)