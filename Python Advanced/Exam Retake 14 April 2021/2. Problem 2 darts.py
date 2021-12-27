def in_side(r, c, s):
    if 0 <= r < s and 0 <= c < s:
        return True
    return False


def get_turn():
    turn_string = input()
    vals = turn_string[1:-1].split(", ")
    return [int(val) for val in vals]


def get_value(r, c, m):
    value_str = m[r][c]
    if value_str.isdigit():
        return int(value_str)

    value = int(m[r][0]) + int(m[r][-1]) + int(m[0][col]) + int(m[-1][col])

    if value_str == "T":
        return value * 3
    elif value_str == "D":
        return value * 2
    elif value_str == "B":
        return 501


size = 7

player_names = input().split(", ")
current_player = player_names[0], 501, 0
other_player = player_names[1], 501, 0

matrix = []
for _ in range(size):
    matrix.append(input().split())

while True:
    row, col = get_turn()
    name, points, turns = current_player

    if not in_side(row, col, size):
        current_player, other_player = other_player, current_player
        continue

    current_points = get_value(row, col, matrix)
    points -= current_points
    turns += 1
    current_player = name, points, turns

    if points <= 0:
        break

    current_player, other_player = other_player, current_player

name, _, turns = current_player
print(f"{name} won the game with {turns} throws!")