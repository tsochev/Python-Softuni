lost_fight = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

aureus_count = 0

for fight in range(1, lost_fight + 1):
    if fight % 2 == 0:
        aureus_count += helmet_price
    if fight % 3 == 0:
        aureus_count += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        aureus_count += shield_price
    if fight % 12 == 0:
        aureus_count += armor_price
print(f"Gladiator expenses: {aureus_count:.2f} aureus")
