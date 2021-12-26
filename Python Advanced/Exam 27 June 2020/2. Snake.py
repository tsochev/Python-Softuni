def is_in_territory(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def get_next_position(direction, r, c):
    if direction == "right":
        return r, c + 1
    if direction == "left":
        return r, c - 1
    if direction == "up":
        return r - 1, c
    if direction == "down":
        return r + 1, c


size = int(input())

matrix = []

snake_row = 0
snake_col = 0
b_row, b_col = 0, 0

for row in range(size):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(size):
        el = row_elements[col]
        if el == "S":
            snake_row, snake_col = row, col
        if el == "B":
            b_row, b_col = row, col

food_quantity = 0

while True:
    line = input()
    path = []
    matrix[snake_row][snake_col] = "."
    snake_row, snake_col = get_next_position(line, snake_row, snake_col)

    if not is_in_territory(snake_row, snake_col, size):
        print("Game over!")
        break

    if matrix[snake_row][snake_col] == "*":
        food_quantity += 1

    if matrix[snake_row][snake_col] == "B":
        matrix[snake_row][snake_col] = "."
        snake_row, snake_col = b_row, b_col
        matrix[snake_row][snake_col] = "S"

    matrix[snake_row][snake_col] = "S"

    if food_quantity == 10:
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food_quantity}")
for r in matrix:
    print(f"{''.join(r)}")