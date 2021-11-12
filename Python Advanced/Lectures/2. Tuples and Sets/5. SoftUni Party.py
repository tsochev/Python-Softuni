n = int(input())

people = set()

# guest_list = {input() for _ in range(n)}
for _ in range(n):
    command = input()
    people.add(command)

while True:
    command = input()
    if command == "END":
        break
    people.remove(command)


def is_vip(guest):
    return guest[0].isdigit()


vip_guests = sorted([g for g in people if is_vip(g)])
regular_guests = sorted([g for g in people if not is_vip(g)])

print(len(people))
[print(g) for g in vip_guests]
[print(g) for g in regular_guests]

