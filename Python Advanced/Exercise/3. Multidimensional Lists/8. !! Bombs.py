def is_inside(r, c, s):
    if 0 <= r < s and 0 <= c < s:
        return True
    return False


def get_bomb_damage(row1, col1, n):
    if is_inside(row1 - 1, col1, n) and matrix[row1 - 1][col1] > 0:
        matrix[row1 - 1][col1] = matrix[row1 - 1][col1] - matrix[row1][col1]
    if is_inside(row1 - 1, col1 - 1, n) and matrix[row1 - 1][col1 - 1] > 0:
        matrix[row1 - 1][col1 - 1] = matrix[row1 - 1][col1 - 1] - matrix[row1][col1]
    if is_inside(row1 - 1, col1 + 1, n) and matrix[row1 - 1][col1 + 1] > 0:
        matrix[row1 - 1][col1 + 1] = matrix[row1 - 1][col1 + 1] - matrix[row1][col1]
    if is_inside(row1, col1 - 1, n) and matrix[row1][col1 - 1] > 0:
        matrix[row1][col1 - 1] = matrix[row1][col1 - 1] - matrix[row1][col1]
    if is_inside(row1, col1 + 1, n) and matrix[row1][col1 + 1] > 0:
        matrix[row1][col1 + 1] = matrix[row1][col1 + 1] - matrix[row1][col1]
    if is_inside(row1 + 1, col1, n) and matrix[row1 + 1][col1] > 0:
        matrix[row1 + 1][col1] = matrix[row1 + 1][col1] - matrix[row1][col1]
    if is_inside(row1 + 1, col1 - 1, n) and matrix[row1 + 1][col1 - 1] > 0:
        matrix[row1 + 1][col1 - 1] = matrix[row1 + 1][col1 - 1] - matrix[row1][col1]
    if is_inside(row1 + 1, col1 + 1, n) and matrix[row1 + 1][col1 + 1] > 0:
        matrix[row1 + 1][col1 + 1] = matrix[row1 + 1][col1 + 1] - matrix[row1][col1]
    matrix[row1][col1] = 0


size = int(input())

matrix = []

for rows in range(size):
    matrix.append([int(x) for x in input().split()])

coordinates = input().split()


for els in coordinates:
    row, col = [int(x) for x in els.split(",")]
    bomb = matrix[row][col]
    if bomb > 0:
        get_bomb_damage(row, col, size)

live_cells = []
sum_of_live_cells = 0

for r in range(size):
    for c in range(size):
        if matrix[r][c] > 0:
            live_cells.append([r, c])
            sum_of_live_cells += matrix[r][c]

print(f"Alive cells: {len(live_cells)}")
print(f"Sum: {sum_of_live_cells}")
for el in matrix:
    print(' '.join([str(x) for x in el]))
