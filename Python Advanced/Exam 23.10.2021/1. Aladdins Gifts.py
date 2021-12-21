from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

succeed = False

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    current_sum = material + magic

    if current_sum < 100:
        if current_sum % 2 == 0:
            material *= 2
            magic *= 3
            current_sum = material + magic
        elif current_sum % 2 != 0:
            current_sum *= 2
    if current_sum > 499:
        material /= 2
        magic /= 2
        current_sum = material + magic

    if 100 <= current_sum <= 199:
        gifts["Gemstone"] += 1
    elif 200 <= current_sum <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= current_sum <= 399:
        gifts["Gold"] += 1
    elif 400 <= current_sum <= 499:
        gifts["Diamond Jewellery"] += 1

    if gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0 \
            or gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0:
        succeed = True

if succeed:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for k, v in sorted(gifts.items()):
    if v > 0:
        print(f"{k}: {v}")
