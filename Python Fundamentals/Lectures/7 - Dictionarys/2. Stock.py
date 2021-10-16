products = input().split()

searched_product = input().split()

bakery = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    bakery[key] = int(value)

for s_p in searched_product:
    if s_p not in bakery:
        print(f"Sorry, we don't have {s_p}")
    else:
        print(f"We have {bakery[s_p]} of {s_p} left")