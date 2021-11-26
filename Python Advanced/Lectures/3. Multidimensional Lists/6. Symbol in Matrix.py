n = int(input())

matrix = []

for _ in range(n):
    row = [x for x in input()]
    matrix.append(row)

sign = input()

location = []
found = False

for row in range(n):
    if found:
        break
    for c in range(n):
        if matrix[row][c] == sign:
            location = [row, c]
            found = True

if found:
    print(f"({location[0]}, {location[1]})")
else:
    print(f"{sign} does not occur in the matrix")