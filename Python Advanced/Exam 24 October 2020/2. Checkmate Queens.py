def in_range(r, c, s):
    if 0 <= r < s and 0 <= c < s:
        return True


directions = {
    "up": (- 1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "right_up": (-1, 1),
    "left_up": (-1, -1),
    "right_down": (1, 1),
    "left_down": (1, -1),
}

size = 8
matrix = []
for row in range(size):
    matrix.append(input().split())

queens = []
queen_row, queen_col = 0, 0
for r in range(size):
    for c in range(size):
        if matrix[r][c] == "Q":
            queen_row, queen_col = r, c
            queens.append([queen_row, queen_col])

queens_succ = []
while queens:
    queen = queens.pop()
    q_row, q_col = queen

    for direction in directions:
        next_row = q_row + directions[direction][0]
        next_col = q_col + directions[direction][1]

        while in_range(next_row, next_col, size):
            if matrix[next_row][next_col] == "K":
                queens_succ.append(queen)
                break

            if matrix[next_row][next_col] == "Q":
                break

            next_row += directions[direction][0]
            next_col += directions[direction][1]

if queens_succ:
    [print(el) for el in queens_succ]
else:
    print("The king is safe!")