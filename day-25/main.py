import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_data = data["Primary Fur Color"]

fur_file = pandas.DataFrame(fur_data.value_counts())
fur_file.to_csv("fur_file_data.csv")


# data = pandas.read_csv("weather_data.csv")
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(celcius_to_ferenheit(monday_temp))
#
