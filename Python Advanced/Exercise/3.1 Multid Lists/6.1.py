def is_outside(b_row, b_col, size):
    if 0 <= b_row < size and 0 <= b_col < size:
        return False
    return True


def get_next_position(move, row, col, steps = 1):
    if move == "up":
        return row - steps, col
    if direction == "down":
        return row + steps, col
    if direction == "left":
        return row, col - steps
    if direction == "right":
        return row, col + steps


size = 5

matrix = []
targets = 0
# WE take the player position.
player_row, player_col = 0, 0
for r in range(size):
    elements = input().split()
    matrix.append(elements)
    for c in range(size):
        element = elements[c]
        if element == "A":
            player_row, player_col = r, c
        if element == "x":
            targets += 1

num_commands = int(input())
targets_position = []

hit_targets = 0

for _ in range(num_commands):
    line = input().split()
    command = line[0]
    direction = line[1]

    if command == "shoot":
        bullet_row, bullet_col = get_next_position(direction, player_row, player_col, 1)
        while True:
            if is_outside(bullet_row, bullet_col, size):
                break
            if matrix[bullet_row][bullet_col] == "x":
                targets_position.append([bullet_row, bullet_col])
                hit_targets += 1
                matrix[bullet_row][bullet_col] = "."
                break
            bullet_row, bullet_col = get_next_position(direction, player_row, player_col, 1)

    if command == "move":
        steps = int(line[2])
        next_player_row, next_player_col = get_next_position(direction, player_row, player_col, steps)

        if is_outside(next_player_row, next_player_col, size):
            continue
        if matrix[next_player_row][next_player_col] != ".":
            continue

        matrix[player_row][player_col] = "."
        matrix[next_player_row][next_player_col] = "A"
        player_row, player_col = next_player_row, next_player_col


if hit_targets == targets:
    print(f"Training completed! All {hit_targets} targets hit.")
else:
    print(f"Training not completed! {targets - hit_targets} targets left.")

[print(x) for x in targets_position]
