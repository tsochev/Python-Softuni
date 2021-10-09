n = int(input())
for first in range(1, n + 1):
    for second in range(1, n + 1):
        for third in range(1, n + 1):
            print(f"{chr(96 + first)}{chr(96 + second)}{chr(96 + third)}")
