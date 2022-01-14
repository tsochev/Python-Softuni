def is_inside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
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

# we take the position of Alice.
alice_row, alice_col = 0, 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "A":
            alice_row, alice_col = row, col

tea_bags = 0
matrix[alice_row][alice_col] = "*"

while True:
    command = input()
    alice_row, alice_col = get_next_position(command, alice_row, alice_col)
    if not is_inside(alice_row, alice_col, size):
        break

    cell_value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = "*"

    if cell_value == "R":
        break

    if cell_value.isdigit():
        tea_bags += int(cell_value)
        if tea_bags >= 10:
            break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(' '.join(x)) for x in matrix]
