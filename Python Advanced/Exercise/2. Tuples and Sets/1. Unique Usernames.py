n = int(input())

# guest_list = {input() for _ in range(n)}
usernames = {input() for _ in range(n)}

[print(g) for g in usernames]