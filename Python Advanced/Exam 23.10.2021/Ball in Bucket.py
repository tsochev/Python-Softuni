import sys


def in_range(r, c, s):
    if 0 <= r < s and 0 <= c < s:
        return True
    return False


size = 6

board = []

bucket_positions = []

for r in range(size):
    board.append(input().split())
    for c in range(size):
        if board[r][c] == "B":
            bucket_positions.append([r, c])

directions = {
    "up": (-1, 0),
    "down": (+1, 0),
}

prize = {
    "Football": range(100, 199),
    "Teddy Bear": range(200, 299),
    "Lego Construction Set": range(300, sys.maxsize),
}

football = 0
teddy_bear = 0
lego = 0

throw_coordinates = []
points = 0
throws = 0
while throws < 3:
    coordinates = input()[1:-1].split(", ")
    row, col = int(coordinates[0]), int(coordinates[1])

    if [row, col] in throw_coordinates:
        throws += 1
        continue

    throw_coordinates.append([row, col])

    if in_range(row, col, size) and board[row][col] == "B":
        for direction in directions:
            next_row = row + directions[direction][0]
            next_col = col + directions[direction][1]

            while in_range(next_row, next_col, size):
                points += int(board[next_row][next_col])

                next_row = next_row + directions[direction][0]
                next_col = next_col + directions[direction][1]

    throws += 1

if 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
