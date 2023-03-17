# with open("./weather_data.csv") as file:
#    data = file.readlines()
#    print(data)

# import csv
#
# with open("./weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

# data = pandas.read_csv("./weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# rint(data_dict)

# Get Data by Columns
# average_temp = data["temp"].mean()
# print(average_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# mon_temp = int(monday.temp)
# print(float(mon_temp) * 1.8 + float(32))

# Create a dataframe from scratch
# data_dict = {
#    "students" : ["Amy", "James", "Angela"],
#    "scores" : [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
fur_list = fur_color.to_list()

#print(fur_list)

fur_dict = {
    "fur color": ["Gray", "Black", "Cinnamon" ],
    "count" : [fur_list.count("Gray"), fur_list.count("Black"), fur_list.count("Cinnamon")],
}

data_fur = pandas.DataFrame(fur_dict)
data_fur.to_csv("squirrel_count.csv")
print(data_fur)
