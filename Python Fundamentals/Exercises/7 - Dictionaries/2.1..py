resources = {}

data = input()
while not data == "stop":
    if data not in resources:
        resources[data] = 0

    qty = int(input())
    resources[data] += qty

    data = input()

for k, v in resources.items():
    print(f"{k} -> {v}")
