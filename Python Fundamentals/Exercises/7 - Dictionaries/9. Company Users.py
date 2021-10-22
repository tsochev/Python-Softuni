comp_info = {}

data = input()
while not data == "End":
    company, employee_id = data.split(" -> ")

    if company not in comp_info:
        comp_info[company] = []

    if employee_id not in comp_info[company]:
        comp_info[company].append(employee_id)

    data = input()

for k, v in sorted(comp_info.items(), key=lambda x: x[0]):
    print(f"{k}")
    for el in v:
        print(f"-- {el}")