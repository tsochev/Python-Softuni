def is_valid(r, c, rows, cols):
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return False
    return True


row, col = [int(x) for x in input().split()]

matrix = []

for _ in range(row):
    matrix.append([x for x in input().split()])

while True:
    line = input()
    if line == "END":
        break
    args = line.split()
    if args[0] != "swap" or len(args) != 5:
        print("Invalid input!")
        continue
    row1, col1, row2, col2 = [int(x) for x in args[1:]]
    if not is_valid(row1, col1, row, col) or not is_valid(row2, col2, row, col):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    [print(' '.join([str(x) for x in x])) for x in matrix]
