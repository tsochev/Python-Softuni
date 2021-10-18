items = input().split("|")
budget = float(input())
new_price = []
profit = 0
money_won = 0

for el in items:
    item_info = el.split("->")
    item = item_info[0]
    price = float(item_info[1])
    if item == "Clothes" and price <= 50.00:
        if budget >= price:
            budget -= price
            over_price = price * 1.40
            money_won += over_price
            profit += over_price - price
            new_price.append("{:.2f}".format(over_price))
    elif item == "Shoes" and price <= 35.00:
        if budget >= price:
            budget -= price
            over_price = price * 1.40
            money_won += over_price
            profit += over_price - price
            new_price.append("{:.2f}".format(over_price))
    elif item == "Accessories" and price <= 20.50:
        if budget >= price:
            budget -= price
            over_price = price * 1.40
            money_won += over_price
            profit += over_price - price
            new_price.append("{:.2f}".format(over_price))

for i in new_price:
    print(f"{i}", end=" ")
print(sep="\n")
print(f"Profit: {profit:.2f}")
if money_won + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
