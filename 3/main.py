import pandas as pd

data = pd.read_csv(r'3\data.csv', sep = ',', header=None)
A = data.loc[0,:].tolist()
B = data.loc[1,:].tolist()

# part 1
x_directions = {'L': -1,
                'R': 1,
                'U': 0,
                'D': 0}

y_directions = {'L': 0,
                'R': 0,
                'U': 1,
                'D': -1}

def draw_grid(directions):
    x, y, length = 0, 0, 0
    final = {}
    for direction in directions:
        d = direction[0]
        k = int(direction[1:])
        for i in range(k):
            x += x_directions[d]
            y += y_directions[d]
            length += 1
            if not (x,y) in final:
                final[(x,y)] = length
    return final

A_positions = draw_grid(A)
B_positions = draw_grid(B)

intersects = (A_positions.keys() & B_positions.keys())
answer = min(abs(x) + abs(y) for (x,y) in intersects)
print(answer)

# part 2
answer = min(A_positions[i] + B_positions[i] for i in intersects)
print(answer)