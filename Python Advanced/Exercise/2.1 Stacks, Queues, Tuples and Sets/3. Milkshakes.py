from collections import deque

chocolates = deque([int(x) for x in input().split(", ")])
cups_milk = deque([int(x) for x in input().split(", ")])

shake = 0

while chocolates and cups_milk and shake < 5:
    chocolate = chocolates.pop()
    cup_of_milk = cups_milk.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue

    if chocolate <= 0:
        cups_milk.appendleft(cup_of_milk)
        continue
    if cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        shake += 1
    else:
        cups_milk.append(cup_of_milk)
        chocolates.append(chocolate - 5)

if shake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_milk])}")
else:
    print("Milk: empty")