# def get_sum_matrix(matrix, r ,c)
#     return matrix[r][c] + \
#            matrix[r][c + 1] + \
#            matrix[r][c + 2] + \
#            matrix[r + 1][c] + \
#            matrix[r + 1][c + 1] + \
#            matrix[r + 1][c + 2] + \
#            matrix[r + 2][c] + \
#            matrix[r + 2][c + 1] + \
#            matrix[r + 2][c + 2]
#

n, m = [int(x) for x in input().split()]

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

max_sum = 0
best_row = 0
best_col = 0
for r in range(n - 2):
    for c in range(m - 2):
        sum_matrix = matrix[r][c] + \
                     matrix[r][c + 1] + \
                     matrix[r][c + 2] + \
                     matrix[r + 1][c] + \
                     matrix[r + 1][c + 1] + \
                     matrix[r + 1][c + 2] + \
                     matrix[r + 2][c] + \
                     matrix[r + 2][c + 1] + \
                     matrix[r + 2][c + 2]
        # sum_matrix = get_sum_matrix(matrix, r , c)
        if sum_matrix > max_sum:
            max_sum, best_row, best_col = sum_matrix, r, c

print(f"Sum = {max_sum}")
print(matrix[best_row][best_col], matrix[best_row][best_col + 1], matrix[best_row][best_col + 2])
print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1], matrix[best_row + 1][best_col + 2])
print(matrix[best_row + 2][best_col], matrix[best_row + 2][best_col + 1], matrix[best_row + 2][best_col + 2])