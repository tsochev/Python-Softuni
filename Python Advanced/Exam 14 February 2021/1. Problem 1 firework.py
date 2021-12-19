from collections import deque


def perfect_show(fireworks):
    return fireworks["palm"] >= 3 and fireworks["willow"] >= 3 and fireworks["crossette"] >= 3


def print_fireworks(fireworks):
    print(f"Palm Fireworks: {fireworks['palm']}")
    print(f"Willow Fireworks: {fireworks['willow']}")
    print(f"Crossette Fireworks: {fireworks['crossette']}")


firework_effect = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

fireworks = {
    "palm": 0,
    "willow": 0,
    "crossette": 0,
}

while firework_effect and explosive_power and not perfect_show(fireworks):

    effect = firework_effect.popleft()
    power = explosive_power.pop()

    if effect <= 0:
        explosive_power.append(power)
        continue
    if power <= 0:
        firework_effect.appendleft(effect)
        continue

    current_sum = effect + power

    if current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks["crossette"] += 1
    elif current_sum % 5 == 0:
        fireworks["willow"] += 1
    elif current_sum % 3 == 0:
        fireworks["palm"] += 1
    else:
        firework_effect.append(effect - 1)
        explosive_power.append(power)

if perfect_show(fireworks):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effect:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effect)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

print_fireworks(fireworks)