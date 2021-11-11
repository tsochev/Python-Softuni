n = int(input())

parking = set()

for _ in range(n):
    direction, car_num = input().split(", ")

    if direction == "IN":
        parking.add(car_num)
    else:
        parking.remove(car_num)

if parking:
    for n in parking:
        print(n)
else:
    print("Parking Lot is Empty")