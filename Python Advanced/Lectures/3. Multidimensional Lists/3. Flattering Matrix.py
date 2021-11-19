rows = int(input())

matrix = []
flatted = []

for row in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)
    # flatted = [num for row in matrix for num in row]

for row in matrix:
    for el in row:
        flatted.append(el)

print(flatted)