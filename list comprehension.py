from itertools import product

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

all_coords = product(range(X+1), range(Y+1), range(Z+1))

result = [list(coord) for coord in all_coords if sum(coord) != N]

print(result)
