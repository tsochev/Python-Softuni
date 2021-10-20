numbers = [int(el) for el in input().split(", ")]
group = 10
while len(numbers) > 0:
    list_nums = [x for x in numbers if x <= group]
    print(f"Group of {group}: {list_nums}")
    numbers = [x for x in numbers if x not in list_nums]
    group += 10
