rows = int(input())

matrix = []

for row in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)
evens = [[x for x in line if x % 2 == 0] for line in matrix]

print(evens)
