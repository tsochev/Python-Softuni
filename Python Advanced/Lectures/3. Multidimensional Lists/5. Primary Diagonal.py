size = int(input())

matrix = []

# ///////// works together //////////
# matrix = [[0] * size for row in range(0, size)]
# for x in range(0, size):
#     line = [int(x) for x in input().split()]
#     for y in range(0, size):
#         matrix[x][y] = line[y]

for _ in range(size):
    row = [int(x) for x in input().split()]
    matrix.append(row)

# 11  2   3
# 4   5   6
# 10  8 -12

sum_diagonal = 0
for r in range(size):
    sum_diagonal += matrix[r][r]

print(sum_diagonal)