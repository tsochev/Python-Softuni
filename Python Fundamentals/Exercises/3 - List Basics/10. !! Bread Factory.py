initial_energy = 100
initial_coins = 100
is_bankrupt = False
events = input(). split("|")

for event in events:
    event_info = event.split("-")
    type_event = event_info[0]
    number_event = int(event_info[1])
    if type_event == "rest":
        energy_gained = number_event
        if initial_energy + number_event > 100:
            energy_gained = 100 - initial_energy
        initial_energy += energy_gained
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {initial_energy}.")
    elif type_event == "order":
        if initial_energy - 30 >= 0:
            initial_coins += number_event
            initial_energy -= 30
            print(f"You earned {number_event} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins - number_event > 0:
            initial_coins -= number_event
            print(f"You bought {type_event}.")
        else:
            is_bankrupt = True
            print(f"Closed! Cannot afford {type_event}.")
            break
if not is_bankrupt:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")