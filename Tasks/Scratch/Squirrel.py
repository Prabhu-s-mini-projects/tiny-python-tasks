import pandas

# CONSTANTS
PATH = "Squirrel_Data.csv"

squirrel_data = pandas.read_csv(PATH)

print(squirrel_data["Primary Fur Color"])

primary_fur_color = squirrel_data["Primary Fur Color"]
# grey = primary_fur_color[primary_fur_color["Primary Fur Color"] == "Gray"]
# red = primary_fur_color[primary_fur_color["Primary Fur Color"] == "Cinnamon"]
# black = primary_fur_color[primary_fur_color["Primary Fur Color"] == "Black"]

#
gray_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
red_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
Black_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

print (type(gray_color))

new_data = {
    "colors": ["gray","red","black"],
    "count": [len(gray_color),len(red_color),len(Black_color)]
}

new_table = pandas.DataFrame(new_data)
new_table.to_csv("squirrel.csv")

print(new_table)
