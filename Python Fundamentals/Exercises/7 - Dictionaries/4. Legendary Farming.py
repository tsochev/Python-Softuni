def collect_material(materials_dict: dict, junk_dict: dict, material: str, qty: int):
    if material == "shards" or material == "fragments" or material == "motes":
        materials_dict[material] += qty
    else:
        if material not in junk_dict:
            junk_dict[material] = qty
        else:
            junk_dict[material] += qty


materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
item_obtained = ""

while item_obtained == "":
    current_line = input().split()

    for i in range(0, len(current_line), 2):
        material_name = current_line[i + 1].lower()
        material_qty = int(current_line[i])

        collect_material(materials, junk, material_name, material_qty)

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