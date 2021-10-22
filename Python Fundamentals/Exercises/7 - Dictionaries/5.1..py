total_products = {}
data = input()
while not data == "buy":
    product, price, qty = data.split()
    price = float(price)
    qty = int(qty)

    if product not in total_products:
        total_products[product] = {"price": price, "qty": qty}
    else:
        total_products[product]["qty"] += qty
        total_products[product]["price"] = price

    data = input()

for k, v in total_products.items():
    result = v["price"] * v["qty"]
    print(f"{k} -> {result:.2f}")