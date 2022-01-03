def in_range(r, c, m):
    size = len(m)
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def bombs_added(r, c, m):
    if in_range(r - 1, c, m):  # up
        if matrix[r - 1][c] != "*":
            matrix[r - 1][c] += 1
    if in_range(r + 1, c, m):  # down
        if matrix[r + 1][c] != "*":
            matrix[r + 1][c] += 1
    if in_range(r, c - 1, m):  # left
        if matrix[r][c - 1] != "*":
            matrix[r][c - 1] += 1
    if in_range(r, c + 1, m):  # right
        if matrix[r][c + 1] != "*":
            matrix[r][c + 1] += 1
    if in_range(r - 1, c + 1, m):  # right_up
        if matrix[r - 1][c + 1] != "*":
            matrix[r - 1][c + 1] += 1
    if in_range(r - 1, c - 1, m):  # left_up
        if matrix[r - 1][c - 1] != "*":
            matrix[r - 1][c - 1] += 1
    if in_range(r + 1, c + 1, m):  # right_down
        if matrix[r + 1][c + 1] != "*":
            matrix[r + 1][c + 1] += 1
    if in_range(r + 1, c - 1, m):  # left_down
        if matrix[r + 1][c - 1] != "*":
            matrix[r + 1][c - 1] += 1


matrix_size = int(input())
bombs = int(input())

matrix = []

for row in range(matrix_size):
    matrix.append([0] * matrix_size)

# around_the_bomb = {
#     "up": lambda r, c: (r - 1, c),
#     "down": lambda r, c: (r + 1, c),
#     "left": lambda r, c: (r, c - 1),
#     "right": lambda r, c: (r, c + 1),
#     "right_up": lambda r, c: (r - 1, c + 1),
#     "left_up": lambda r, c: (r - 1, c - 1),
#     "right_down": lambda r, c: (r + 1, c + 1),
#     "left_down": lambda r, c: (r + 1, c - 1),
# }

while bombs > 0:
    coordinates = input()
    row, col = [int(x) for x in coordinates[1:-1].split(", ")]

    if in_range(row, col, matrix):
        matrix[row][col] = "*"

    bombs_added(row, col, matrix)

    bombs -= 1

for row in matrix:
    print(" ".join([str(x) for x in row]))


