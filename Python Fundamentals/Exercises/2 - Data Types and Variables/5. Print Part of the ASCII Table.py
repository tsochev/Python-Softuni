start_char = int(input())
last_char = int(input())

for index in range(start_char, last_char + 1):
    symbol = chr(index)
    print(f"{symbol}", end=" ")
