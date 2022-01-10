n, m = [int(x) for x in input().split()]

matrix = []

for _ in range(n):
    matrix.append([x for x in input().split()])

squares = 0
for r in range(n - 1):
    for c in range(m - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            squares += 1

print(squares)
