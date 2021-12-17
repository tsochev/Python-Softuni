from collections import deque

bees = deque([int(x) for x in input().split()])  # take first bee
nectar = [int(x) for x in input().split()]  # take last nectar
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    bee = bees.popleft()
    amount_nectar = nectar.pop()

    if amount_nectar >= bee:
        symbol = symbols.popleft()
        if symbol == "+":
            total_honey += abs(bee + amount_nectar)
        elif symbol == "-":
            total_honey += abs(bee - amount_nectar)
        elif symbol == "*":
            total_honey += abs(bee * amount_nectar)
        elif symbol == "/":
            if amount_nectar > 0:
                total_honey += abs(bee / amount_nectar)
    else:
        bees.appendleft(bee)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")