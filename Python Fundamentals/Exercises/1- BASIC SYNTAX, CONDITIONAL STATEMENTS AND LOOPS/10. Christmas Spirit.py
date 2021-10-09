quantity = int(input())
days_left = int(input())
ornament_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_light_price = 15
budget = 0
spirit_count = 0
for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += ornament_price * quantity
        spirit_count += 5
    if day % 3 == 0:
        budget += (tree_skirt_price + tree_garlands_price) * quantity
        spirit_count += 13
    if day % 5 == 0:
        budget += tree_light_price * quantity
        spirit_count += 17
        if day % 3 == 0:
            spirit_count += 30
    if day % 10 == 0:
        spirit_count -= 20
        budget += tree_skirt_price + tree_garlands_price + tree_light_price
if days_left % 10 == 0:
    spirit_count -= 30


print(f"Total cost: {budget}")
print(f"Total spirit: {spirit_count}")
