import pandas
import pandas as pd
# data = pd.read_csv("./weather_data.csv")
# print(round(data.temp.mean(),3))
#
# # get row
# print(data[data.condition == "Sunny"])
#
# print(data[data.temp == data.temp.min()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_f = monday_temp*9/5
# print(monday.temp)
# print(monday_f)

# data_dict = {
#     "students": ["Amy", "James", "Johny"],
#     "scores": [65, 78, 99]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_csv")
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_number = len(data[data["Primary Fur Color"] == "Gray"])
black_number = len(data[data["Primary Fur Color"] == "Black"])
red_number = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dic = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [black_number, red_number, gray_number]
}

table = pandas.DataFrame(data_dic)
table.to_csv("Squirrel Data.csv")
