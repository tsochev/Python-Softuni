def are_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == "END":
        break
    args = line.split()
    row, col, value = [int(x) for x in args[1:]]

    if args[0] == "Add":
        if not are_valid(row, col, size):
            print("Invalid coordinates")
            continue

        matrix[row][col] += value

    elif args[0] == "Subtract":
        if not are_valid(row, col, size):
            print("Invalid coordinates")
            continue

        matrix[row][col] -= value

for row in matrix:
    print(' '.join([str(x) for x in row]))