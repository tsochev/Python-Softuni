from collections import deque

bomb_effect = deque([int(el) for el in input().split(", ")])
bomb_casting = deque([int(el) for el in input().split(", ")])

bombs = {
    "Datura Bombs": [40, 0],
    "Cherry Bombs": [60, 0],
    "Smoke Decoy Bombs": [120, 0],
}

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0

ezio_succ = False

while True:
    if not bomb_effect or not bomb_casting:
        break
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        ezio_succ = True
        break

    effect = bomb_effect.popleft()
    casting = bomb_casting.pop()
    both_sum = effect + casting

    if both_sum == bombs["Datura Bombs"][0]:
        bombs["Datura Bombs"][1] += 1
        datura_bombs += 1
    elif both_sum == bombs["Cherry Bombs"][0]:
        bombs["Cherry Bombs"][1] += 1
        cherry_bombs += 1
    elif both_sum == bombs["Smoke Decoy Bombs"][0]:
        bombs["Smoke Decoy Bombs"][1] += 1
        smoke_decoy_bombs += 1
    else:
        bomb_effect.appendleft(effect)
        bomb_casting.append(casting - 5)


if ezio_succ:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effect])}")
else:
    print("Bomb Effects: empty")

if bomb_casting:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casting])}")
else:
    print("Bomb Casings: empty")

for key, val in sorted(bombs.items()):
    print(f"{key}: {val[1]}")
