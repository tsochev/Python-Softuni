def in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def next_position(direction, r, c):
    if direction == "right":
        return r, c + 1
    if direction == "left":
        return r, c - 1
    if direction == "up":
        return r - 1, c
    if direction == "down":
        return r + 1, c


directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
}

text = input()
size = int(input())
mtx = []

p_row, p_col = 0, 0
for row in range(size):
    row_el = list(input())
    mtx.append(row_el)
    for col in range(size):
        if mtx[row][col] == "P":
            p_row, p_col = row, col

turns = int(input())

while turns > 0:
    command = input()
    old_row, old_col = p_row, p_col
    p_row, p_col = next_position(command, p_row, p_col)
    if in_range(p_row, p_col, size):
        mtx[old_row][old_col] = "-"
        if str(mtx[p_row][p_col]).isalpha():
            text += mtx[p_row][p_col]

    else:
        text = text[:-1]
        p_row, p_col = old_row, old_col
    mtx[p_row][p_col] = "P"
    turns -= 1

print(text)
[print(''.join(row)) for row in mtx]
# for row in mtx:
#     print("".join([str(x) for x in row]))
