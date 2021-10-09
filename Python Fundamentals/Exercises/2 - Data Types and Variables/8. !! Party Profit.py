party_size = int(input())
days = int(input())

coins_count = 0

for i in range(1, days + 1):

    if i % 15 == 0:
        party_size += 5
    if i % 10 == 0:
        party_size -= 2
    coins_count += 50 - (party_size * 2)
    if i % 3 == 0:
        coins_count -= party_size * 3
    if i % 5 == 0:
        coins_count += party_size * 20
        if i % 3 == 0:
            coins_count -= party_size * 2
coins_per_companion = int(coins_count / party_size)
print(f"{party_size} companions received {coins_per_companion} coins each.")
