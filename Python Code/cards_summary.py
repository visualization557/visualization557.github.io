from os.path import join
from csv import reader
import matplotlib.pyplot as plt
import numpy as np


path = './assignment2/'
# process employees data
employees_dic = {}
type_dic = {
    "Engineering": 0,
    "Executive": 1,
    "Facilities": 2,
    "Information Technology": 3,
    "Security": 4}

legend_color = ["#DE3163","#FF7F50","#FFBF00","#9FE2BF","#40E0D0","#6495ED"]
types = ["Engineering", "Executive", "Facilities", "Information Technology", "Security"]

# extract employee name, employment type and car ID
# employment type: Engineering, Executive, Facilities, Information Technology, Security
with open(join(path, 'car-assignments.csv'), encoding="ISO-8859-1") as f:
    csv_reader = reader(f)
    next(csv_reader) # skip header
    for row in csv_reader:
        last = row[0]
        first = row[1]
        name = first + " " + last
        if row[2] == "":
            car_id = 0 # 0 if none
        else:
            car_id = row[2]
        e_type = row[3]
        employees_dic[name] = [car_id, e_type]


# process cards data
def loc_freq_avg_price_analysis(filename, prompt):

    loc_dic = {}
    loc = []
    eng_freq = []
    exe_freq = []
    fac_freq = []
    it_freq = []
    sec_freq = []
    other_freq = []
    avg_price = []

    # extract location and price info from csv file
    with open(join(path, filename), encoding="ISO-8859-1") as f:
        csv_reader = reader(f)
        next(csv_reader) # skip header
        for row in csv_reader:
            location = row[1]
            price = row[2]
            first = row[3]
            last = row[4]
            name = first + " " + last
            if name in employees_dic:
                e_type = type_dic[employees_dic[name][1]]
            else:
                e_type = 5
            if location not in loc_dic:
                value = [0, 0, 0, 0, 0, 0, 0]
                loc_dic[location] = value
            loc_dic[location][e_type] += 1
            loc_dic[location][6] += float(price)
            if name in employees_dic:
                if prompt[0] == 'C':
                    if len(employees_dic[name]) == 2:
                        employees_dic[name].append(float(price))
                        employees_dic[name].append(0)
                    else:
                        employees_dic[name][2] += float(price)
                else:
                    if len(employees_dic[name]) == 2:
                        employees_dic[name].append(0)
                        employees_dic[name].append(float(price))
                    else:
                        employees_dic[name][3] += float(price)

    for location, properties in sorted(loc_dic.items()):
        loc.append(location)
        eng_freq.append(properties[0])
        exe_freq.append(properties[1])
        fac_freq.append(properties[2])
        it_freq.append(properties[3])
        sec_freq.append(properties[4])
        other_freq.append(properties[5])
        avg_price.append(round(round(properties[6], 2)/sum(properties[:6]), 2))

    eng_freq = np.array(eng_freq)
    exe_freq = np.array(exe_freq)
    fac_freq = np.array(fac_freq)
    it_freq = np.array(it_freq)
    sec_freq = np.array(sec_freq)
    other_freq = np.array(other_freq)

    # display bar chart for info
    fig = plt.figure(figsize=(20,16))
    fig.canvas.set_window_title(prompt + ' Analysis')
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.bar(loc, eng_freq, color="#DE3163")
    ax1.bar(loc, exe_freq, bottom=eng_freq, color="#FF7F50")
    ax1.bar(loc, fac_freq, bottom=eng_freq+exe_freq, color="#FFBF00")
    ax1.bar(loc, it_freq, bottom=eng_freq+exe_freq+fac_freq, color="#9FE2BF")
    ax1.bar(loc, sec_freq, bottom=eng_freq+exe_freq+fac_freq+it_freq, color="#40E0D0")
    ax1.bar(loc, other_freq, bottom=eng_freq+exe_freq+fac_freq+it_freq+sec_freq, color="#6495ED")
    ax1.set_title(prompt + " Location Frequency")
    ax1.set_xticklabels(loc, rotation=45, ha='right')
    ax1.legend(["Engineering", "Executive", "Facilities", "Information Technology", "Security", "Other"], loc="upper right")

    ax2.bar(loc, avg_price)
    ax2.set_title(prompt + " Location Average Price")
    ax2.set_xticklabels(loc, rotation=45, ha='right')

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.4)
    # plt.show()


loc_freq_avg_price_analysis("cc_data.csv", "Credit Card")
loc_freq_avg_price_analysis("loyalty_data.csv", "Loyalty Card")


# total money spent by each member group by their employment type
employment_by_type = [[],[],[],[],[]]
credit_amount_by_type = [[],[],[],[],[]]
loyalty_amount_by_type = [[],[],[],[],[]]

for employee, properties in employees_dic.items():
    employment_by_type[type_dic[properties[1]]].append(employee)
    credit_amount_by_type[type_dic[properties[1]]].append(round(properties[2],2))
    loyalty_amount_by_type[type_dic[properties[1]]].append(round(properties[3],2))

# display bar chart
fig = plt.figure(figsize=(20,10))
fig.canvas.set_window_title('Money Spent by Employment Type')
for i in range(5):
    ax = fig.add_subplot(1, 5, i+1)
    ax.bar(employment_by_type[i], credit_amount_by_type[i], color=legend_color[i], label=types[i]+" credit")
    ax.bar(employment_by_type[i], loyalty_amount_by_type[i], bottom=credit_amount_by_type[i], color=legend_color[i], label=types[i]+" loyalty", hatch="-")
    ax.set_xticklabels(employment_by_type[i], rotation=45, ha='right')
    ax.legend(loc="upper right")

# plt.show()

