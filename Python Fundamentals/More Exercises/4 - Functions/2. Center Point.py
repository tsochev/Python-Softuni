import math


def coordinates(p1, p2):
    result = abs(p1) + abs(p2)
    return math.floor(result)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

first_point = coordinates(x1, x2)
second_point = coordinates(x2, y2)
if first_point >= second_point:
    print(f"({math.floor(x2)}, {math.floor(y2)})")
else:
    print(f"({math.floor(x1)}, {math.floor(y1)})")
