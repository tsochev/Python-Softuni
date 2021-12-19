import math


def in_range(r, c, s):
    if 0 <= r < s and 0 <= c < s:
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


# directions = {
#     "up": (- 1, 0),
#     "down": (+ 1, 0),
#     "left": (0, - 1),
#     "right": (0, + 1),
# }

size = int(input())
matrix = []

for _ in range(size):
    matrix.append(input().split())

player_row, player_col = 0, 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "P":
            player_row, player_col = row, col

path = []
coins = 0
won = False
while True:
    command = input()
    player_row, player_col = next_position(command, player_row, player_col)

    if not in_range(player_row, player_col, size):
        coins = math.floor(coins / 2)
        break

    if matrix[player_row][player_col] == "X":
        coins = math.floor(coins / 2)
        break

    coins += int(matrix[player_row][player_col])
    path.append([player_row, player_col])

    if coins >= 100:
        won = True
        break

if won:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
[print(x) for x in path]