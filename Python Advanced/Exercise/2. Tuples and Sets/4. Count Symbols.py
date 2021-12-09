text = input()

symbols = {}

for el in text:
    if el not in symbols:
        symbols[el] = 0
    symbols[el] += 1

for el, count in sorted(symbols.items()):
    print(f"{el}: {count} time/s")
