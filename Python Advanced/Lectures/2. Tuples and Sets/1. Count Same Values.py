numbers = [float(x) for x in input().split(" ")]

num_counter = {}

for num in numbers:
    if num not in num_counter:
        num_counter[num] = 1
    else:
        num_counter[num] += 1

for num, count in num_counter.items():
    print(f"{num} - {count} times")