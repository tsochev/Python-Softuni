rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

result = []

for c in range(columns):
    sum_column = 0
    for r in range(rows):
        sum_column += matrix[r][c]
    result.append(sum_column)

[print(x) for x in result]