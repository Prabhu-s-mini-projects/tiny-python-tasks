#Dependenies
import csv
import pandas
from numpy.ma.extras import average

# CONSTANTS
csv_file_path = "weather_data.csv"

def read_file(path:str)-> list:
    with open(path) as csv_file:
        csv_data = csv.reader(csv_file)
        temperatures = []
        for row in csv_data:
            if row[1] != "temp":
                temperatures.append(int(row[1]))
    return temperatures

# fetching the CSV data using CSV
data = read_file(csv_file_path)
print(type(data))
print(data)

# fetching the CSV data using Pandas
data_from_panda = pandas.read_csv(csv_file_path)
print(type(data_from_panda))
print(data_from_panda)
print(data_from_panda["temp"])

data_dict = data_from_panda.to_dict()
print(data_dict)
print(data_dict.keys())
print(data_dict.values())

print(type (data_dict["temp"]))
temp_list = data_from_panda["temp"].to_list()
average_temp = average(temp_list)
print(average_temp)

print(data_from_panda["temp"].mean())
print(temp_list)
print(data_from_panda["temp"].max())
print(data_from_panda["temp"].min())

print(data_from_panda["condition"])
print(data_from_panda.condition)

print(data_from_panda[data_from_panda.day == "Monday"])
print(data_from_panda[data_from_panda.temp == data_from_panda.temp.max()])

monday = data_from_panda[data_from_panda.day =="Monday"]
temp_f = monday.temp[0] * 9/5 +32

print(temp_f)

data_dict = {
    "students" : ["prabhukumar", "monika", "sivamoorthi", "selvi"],
    "scores" : [100,100,100,100]
}

data = pandas.DataFrame(data_dict)
print(data)

