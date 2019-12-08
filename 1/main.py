import pandas as pd
import math

# mass gedeeld door 3 round down substract 2

# part 1
data = pd.read_excel(r'1\data.xlsx', header=None)
listdata = list(data.iloc[:,0])
fuel = [math.floor(x/3) - 2 for x in listdata]
total_fuel = sum(fuel)
print(total_fuel)

# part 2
fuel_list = []

for module in listdata:
    total = []
    fuel = math.floor(module/3) - 2
    total.append(fuel)
    i = 0
    while fuel > 0:
        fuel = math.floor(fuel/3) - 2
        if fuel > 0:
            total.append(fuel)
    fuel_list.append(sum(total))