def price(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "coke":
        return quantity * 1.40
    elif product == "water":
        return quantity
    elif product == "snacks":
        return quantity * 2.00


type_product = input()
count = int(input())
total_price = price(type_product, count)
print(f"{total_price:.2f}")
