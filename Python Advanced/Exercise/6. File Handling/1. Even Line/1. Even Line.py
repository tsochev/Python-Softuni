symbols = {"-", ",", ".", "!", "?"}

with open("text.txt", "r") as file:
    index = 0
    while True:
        line = file.readline().strip()
        if not line:
            break
        if index % 2 != 0:
            index += 1
            continue
        for symbol in symbols:
            line = line.replace(symbol, "@")

        reversed_line = line.split()[::-1]
        print(" ".join(reversed_line))
        index += 1


