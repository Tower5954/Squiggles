import pandas

data = pandas.read_csv("Squirrel_Data_nyc.csv")

gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {

    "Fur Colour": ["Gray", "Red", "Black"],
    "Count": [gray_squirrel, red_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")