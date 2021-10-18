level_fire = input().split("#")
water = int(input())
effort = 0
total_fire = 0
out_of_fire = []

for fire in level_fire:
    fire_info = fire.split(" = ")
    to_num = int(fire_info[1])
    if water < to_num:
        continue
    if fire_info[0] == "High" and 81 <= to_num <= 125:
        water -= to_num
        effort += to_num * 0.25
        total_fire += to_num
        out_of_fire.append(to_num)

    elif fire_info[0] == "Medium" and 51 <= to_num < 81:
        water -= to_num
        effort += to_num * 0.25
        total_fire += to_num
        out_of_fire.append(to_num)

    elif fire_info[0] == "Low" and 1 <= to_num < 51:
        water -= to_num
        effort += to_num * 0.25
        total_fire += to_num
        out_of_fire.append(to_num)


print("Cells:")
for num in out_of_fire:
    print(f" - {num}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
