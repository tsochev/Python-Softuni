n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])

primary = []
secondary = []

for r in range(n):
    primary.append(matrix[r][r])
    secondary.append(matrix[r][n - r - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")