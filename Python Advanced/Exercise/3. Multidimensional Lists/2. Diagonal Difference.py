n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

sum_primary = 0
sum_secondary = 0

for r in range(n):
    sum_primary += matrix[r][r]
    sum_secondary += matrix[r][n - r - 1]

print(abs(sum_primary - sum_secondary))