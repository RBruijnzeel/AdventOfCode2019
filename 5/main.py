import pandas as pd

data2 = pd.read_csv(r'5\data.csv', sep = ',', header=None).T

# part 1
data2 = pd.read_csv(r'2\data.csv', sep = ',', header=None).T
data2.iloc[1,0] = 12
data2.iloc[2,0] = 2


def find_first(data):

    stopping_pos = data[data.iloc[:, 0] == 99].iloc[0, 0]

    for i in range(stopping_pos+1):
        intcode = data.iloc[i*4, 0]
        pos1 = data.iloc[i * 4 + 1, 0]
        pos2 = data.iloc[i * 4 + 2, 0]
        pos3 = data.iloc[i * 4 + 3, 0]
        if intcode == 1:
            data.iloc[pos3, 0] = data.iloc[pos1, 0] + data.iloc[pos2, 0]
        elif intcode == 2:
            data.iloc[pos3, 0] = data.iloc[pos1, 0] * data.iloc[pos2, 0]
        elif intcode == 3:

        elif intcode == 4:

        elif intcode == 99:
            break
        else:
            print('error')

    return data.iloc[0,0]

print(find_first(data2))


# part 2
data2 = pd.read_csv('data.csv', sep=',', header=None).T

def find_vars(data2, verb, noun):
    data = data2.copy()
    data.iloc[1, 0] = verb
    data.iloc[2, 0] = noun

    stopping_pos = data[data.iloc[:, 0] == 99].iloc[0, 0]
    for i in range(stopping_pos + 1):
        intcode = data.iloc[i * 4, 0]
        pos1 = data.iloc[i * 4 + 1, 0]
        pos2 = data.iloc[i * 4 + 2, 0]
        pos3 = data.iloc[i * 4 + 3, 0]
        if intcode == 1:
            data.iloc[pos3, 0] = data.iloc[pos1, 0] + data.iloc[pos2, 0]
        elif intcode == 2:
            data.iloc[pos3, 0] = data.iloc[pos1, 0] * data.iloc[pos2, 0]
        elif intcode == 99:
            break
        else:
            print('error in intcode')
        data.iloc[i*4, 0] = intcode + 3

    return data.iloc[0,0]

for noun in range(100):
    for verb in range(100):
        if find_vars(data2, noun, verb) == 19690720:
            print(noun, verb)

