parking = {}
num_commands = int(input())

while num_commands > 0:
    data = input().split()

    if data[0] == "register":
        name = data[1]
        license_num = data[2]

        if name not in parking:
            parking[name] = license_num
            print(f"{name} registered {license_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_num}")

    elif data[0] == "unregister":
        name = data[1]

        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            parking.pop(name)
    num_commands -= 1

for k, v in parking.items():
    print(f"{k} => {v}")