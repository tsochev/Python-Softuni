money = float(input())
one_kg_flour_price = float(input())
cozonac_counter = 0
eggs_counter = 0
eggs_price = one_kg_flour_price * 0.75
milk_price = one_kg_flour_price * 1.25 / 4
cozonac_price = one_kg_flour_price + eggs_price + milk_price
while money - cozonac_price > 0:
    cozonac_counter += 1
    money -= cozonac_price
    eggs_counter += 3
    if cozonac_counter % 3 == 0:
        eggs_counter -= cozonac_counter - 2

print(f"You made {cozonac_counter} cozonacs! Now you have {eggs_counter} eggs and {money:.2f}BGN left.")

