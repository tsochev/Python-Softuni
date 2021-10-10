n = int(input())

for num in range(1, n + 1):
    num_as_string = str(num)
    result = 0
    for symbol in num_as_string:
        symbol = int(symbol)
        result += symbol
    if result == 5 or result == 7 or result == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
