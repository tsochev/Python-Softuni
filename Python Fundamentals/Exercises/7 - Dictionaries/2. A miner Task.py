data = input()
resources = {}

while not data == "stop":
    if data not in resources:
        resources[data] = 0

    qty = int(input())
    resources[data] += qty
    data = input()

for key, value in resources.items():
    print(f"{key} -> {value}")
