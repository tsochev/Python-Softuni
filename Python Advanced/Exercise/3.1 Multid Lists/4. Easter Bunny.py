def is_inside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


size = int(input())

matrix = []

bunny_row, bunny_col = 0, 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "B":
            bunny_row, bunny_col = row, col

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
}

max_eggs = 0
best_direction = ""
best_path = []

for direction, step in directions.items():
    eggs = 0
    current_row, current_col = bunny_row, bunny_col
    path = []
    while True:
        current_row, current_col = step(current_row, current_col)
        if not is_inside(current_row, current_col, size):
            break
        if matrix[current_row][current_col] == "X":
            break
        eggs += int(matrix[current_row][current_col])
        path.append([current_row, current_col])

    if eggs > max_eggs:
        max_eggs = eggs
        best_direction = direction
        best_path = path

print(best_direction)
[print(x) for x in best_path]
print(max_eggs)