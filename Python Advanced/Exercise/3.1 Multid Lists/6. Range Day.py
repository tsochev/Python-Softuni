def is_inside(b_row, b_col, size):
    if 0 <= b_row < size and 0 <= b_col < size:
        return True


def get_next_position(move, row, col, steps):
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

shooting_direction = {
    "right": lambda r, c: (r, c + 1),
    "down": lambda r, c: (r + 1, c),
    "up": lambda r, c: (r - 1, c),
    "left": lambda r, c: (r, c - 1),
}

hit_targets = 0

for _ in range(num_commands):
    line = input().split()
    command = line[0]
    direction = line[1]

    if command == "shoot":
        step = shooting_direction[direction]
        bullet_row, bullet_col = step(player_row, player_col)
        while True:
            if not is_inside(bullet_row, bullet_col, size):
                break
            if matrix[bullet_row][bullet_col] == "x":
                targets_position.append([bullet_row, bullet_col])
                hit_targets += 1
                matrix[bullet_row][bullet_col] = "."
                break
            bullet_row, bullet_col = step(bullet_row, bullet_col)

    if command == "move":
        steps = int(line[2])
        next_player_row, next_player_col = get_next_position(direction, player_row, player_col, steps)

        if not is_inside(next_player_row, next_player_col, size):
            continue
        if matrix[next_player_row][next_player_col] != ".":
            continue

        matrix[player_row][player_col] = "."
        matrix[next_player_row][next_player_col] = "A"
        player_row, player_col = next_player_row, next_player_col

    if targets == 0:
        break

if hit_targets == targets:
    print(f"Training completed! All {hit_targets} targets hit.")
else:
    print(f"Training not completed! {targets - hit_targets} targets left.")

[print(x) for x in targets_position]
