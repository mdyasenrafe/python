import csv

with open("./data/currencyrates.csv", "r") as file:
    lines = csv.reader(file)
    for line in lines:
        if "Bangladeshi" in line[0]:
            dollar_rate = 84 * float(line[2])
            print(dollar_rate)
