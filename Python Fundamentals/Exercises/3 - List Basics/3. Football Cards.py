cards = input().split()

team_a = 11
team_b = 11
list_a = []
list_b = []
is_playing = True

for el in cards:
    if el[0] == "A":
        if el in list_a:
            continue
        else:
            team_a -= 1
            list_a.append(el)
    if el[0] == "B":
        if el in list_b:
            continue
        else:
            team_b -= 1
            list_b.append(el)
    if team_a < 7 or team_b < 7:
        is_playing = False
        break

if is_playing:
    print(f"Team A - {team_a}; Team B - {team_b}")
else:
    print(f"Team A - {team_a}; Team B - {team_b}")
    print("Game was terminated")
