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
            time = row[0]
            loc = row[1]
            price = row[2]
            if name not in personal_data_dic:
                personal_data_dic[name] = [{},{}]
            loc_time = loc + "-" + time
            if isCredit:
                personal_data_dic[name][0][loc_time] = float(price)
            else:
                personal_data_dic[name][1][loc_time] = float(price)

def generate_personal_data_dic():
    read_file("cc_data.csv", True)
    read_file("loyalty_data.csv", False)

def get_personal_data(name):
    data = personal_data_dic[name]
    credit = data[0]
    loyalty = data[1]

    # money spent record through timeline
    loc_time_seq = []
    credit_amount = []
    loyalty_amount = []

    # join credit data and loyalty data
    for key, amount in credit.items():
        parts = key.split(" ")
        loc_time = (" ").join(parts[:-1])
        loc_time_seq.append(key)
        credit_amount.append(amount)
        if loc_time in loyalty:
            loyalty_amount.append(loyalty.pop(loc_time))
        else:
            loyalty_amount.append(0)

    for key, amount in loyalty.items():
        loc_time_seq.append(key)
        credit_amount.append(0)
        loyalty_amount.append(amount)

    # display bar chart
    fig, ax = plt.subplots(figsize=(20,12))
    ax.set_title('Money Spent by ' + name + ' with location and time')
    y = np.arange(len(loc_time_seq))
    width = 0.40
    credit = ax.barh(y - 0.20, credit_amount, width, label="credit")
    loyalty = ax.barh(y + 0.20, loyalty_amount, width, label="loyalty")
    ax.set_yticks(y)
    ax.set_yticklabels(loc_time_seq)
    ax.legend(loc="upper right")

    ax.bar_label(credit, padding=4, size=8)
    ax.bar_label(loyalty, padding=4, size=8)
    # plt.show()
    plt.savefig("./employee_details/" + name + "_" + "details.png")

generate_personal_data_dic()
for employee in personal_data_dic.keys():
    get_personal_data(employee)