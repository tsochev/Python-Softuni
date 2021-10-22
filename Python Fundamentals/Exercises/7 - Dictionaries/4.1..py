def collect_material(dict_material: dict, junk: dict, material: str, qty: int):
    if material == "shards" or material == "fragments" or material == "motes":
        dict_material[material] += qty
    else:
        if material not in junk:
            junk[material] = qty
        else:
            junk[material] += qty


materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
item_obtained = ""

while item_obtained == "":
    current_line = input().split()

    for i in range(0, len(current_line), 2):
        qty = int(current_line[i])
        name_m = current_line[i + 1].lower()

        collect_material(materials, junk, name_m, qty)

        if materials["shards"] >= 250:
            item_obtained = "Shadowmourne"
            materials["shards"] -= 250
            break
        elif materials["fragments"] >= 250:
            item_obtained = "Valanyr"
            materials["fragments"] -= 250
            break
        elif materials["motes"] >= 250:
            item_obtained = "Dragonwrath"
            materials["motes"] -= 250
            break

print(f"{item_obtained} obtained!")
for k, v in sorted(materials.items(), key=lambda x: (-x[1], x[0])):
    print(f"{k}: {v}")

for k, v in sorted(junk.items(), key=lambda x: x[0]):
    print(f"{k}: {v}")
