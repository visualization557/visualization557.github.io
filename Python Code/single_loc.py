from os.path import join
from csv import reader
import matplotlib.pyplot as plt
import numpy as np

path = './assignment2/'
loc_data_dic = {}

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
            if loc not in loc_data_dic:
                loc_data_dic[loc] = [{},{}]
            employee_time = name + "-" + time
            if isCredit:
                loc_data_dic[loc][0][employee_time] = float(price)
            else:
                loc_data_dic[loc][1][employee_time] = float(price)

def generate_loc_data_dic():
    read_file("cc_data.csv", True)
    read_file("loyalty_data.csv", False)

def get_loc_data(name, isAll):
    data = loc_data_dic[name]
    credit = data[0]
    loyalty = data[1]

    # money spent record through timeline
    employee_time_seq = []
    credit_amount = []
    loyalty_amount = []

    # join credit data and loyalty data
    for key, amount in credit.items():
        parts = key.split(" ")
        employee_time = (" ").join(parts[:-1])

        # all records
        if isAll:
            employee_time_seq.append(key)
            credit_amount.append(amount)
            if employee_time in loyalty:
                loyalty_amount.append(loyalty.pop(employee_time))
            else:
                loyalty_amount.append(0)
        # just credit
        else:
            if employee_time not in loyalty:
                employee_time_seq.append(key)
                credit_amount.append(amount)
                loyalty_amount.append(0)
            else:
                loyalty.pop(employee_time)

    # just loyalty
    for key, amount in loyalty.items():
        employee_time_seq.append(key)
        credit_amount.append(0)
        loyalty_amount.append(amount)

    # display bar chart
    fig, ax = plt.subplots(figsize=(20,12))
    ax.set_title('Records in ' + name)
    y = np.arange(len(employee_time_seq))
    width = 0.40
    credit = ax.barh(y - 0.20, credit_amount, width, label="credit")
    loyalty = ax.barh(y + 0.20, loyalty_amount, width, label="loyalty")
    ax.set_yticks(y)
    ax.set_yticklabels(employee_time_seq)
    ax.legend(loc="upper right")

    ax.bar_label(credit, padding=4, size=8)
    ax.bar_label(loyalty, padding=4, size=8)
    # plt.show()
    if isAll:
        plt.savefig("./location_full/" + name + "_" + "full.png")
    else:
        plt.savefig("./location_only/" + name + "_" + "only.png")

generate_loc_data_dic()
for location in loc_data_dic.keys():
    get_loc_data(location, True)
    get_loc_data(location, False)