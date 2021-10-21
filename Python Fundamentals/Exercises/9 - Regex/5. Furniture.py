import re


pattern = r"^>>(?P<furniture>\w+)<<(?P<price>\d+\.*[0-9]*)!(?P<quantity>\d+)$"
bought_furniture = []
total_price = 0

text = input()
while not text == "Purchase":
    matches = re.match(pattern, text)

    if matches is not None:
        furniture_name = matches.group('furniture')
        price_furniture = float(matches.group('price'))
        quantity = int(matches.group('quantity'))

        bought_furniture.append(furniture_name)
        total_price += price_furniture * quantity

    text = input()

print("Bought furniture:")
for match in bought_furniture:
    print(match)
print(f"Total money spend: {total_price:.2f}")
