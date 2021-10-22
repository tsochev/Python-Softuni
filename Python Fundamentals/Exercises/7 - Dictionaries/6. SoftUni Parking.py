commands = int(input())
register = {}

while commands > 0:
    data = input().split()

    if data[0] == "register":
        if data[1] not in register:
            register[data[1]] = data[2]
            print(f"{data[1]} registered {data[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {data[2]}")

    elif data[0] == "unregister":
        if data[1] not in register:
            print(f"ERROR: user {data[1]} not found")
        else:
            print(f"{data[1]} unregistered successfully")
            register.pop(data[1])

    commands -= 1


for k, v in register.items():
    print(f"{k} => {v}")