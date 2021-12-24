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


king_row, king_col = 0, 0
for r in range(size):
    for c in range(size):
        if matrix[r][c] == "K":
            king_row, king_col = r, c

queens = []
while True:
    for direction in directions:
        next_row = king_row + directions[direction][0]
        next_col = king_col + directions[direction][1]

        while in_range(next_row, next_col, size):
            if matrix[next_row][next_col] == "Q":
                queens.append([next_row, next_col])
                break

            next_row += directions[direction][0]
            next_col += directions[direction][1]
    break

if queens:
    [print(el) for el in queens]
else:
    print("The king is safe!")
