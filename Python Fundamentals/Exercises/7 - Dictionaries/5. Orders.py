data = input()

products_info = {}

while not data == "buy":
    cmd = data.split()
    name = cmd[0]
    price = float(cmd[1])
    qty = int(cmd[2])

    if name not in products_info:
        products_info[name] = {"price": price, "qty": qty}
        data = input()
        continue

    products_info[name]['price'] = price
    products_info[name]["qty"] += qty

products = {k: v["price"] * v["qty"] for k, v in products_info.items()}

for k, v in products.items():
    print(f"{k} -> {v:.2f}")