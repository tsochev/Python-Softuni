def combinations(values, index, count, comb):
    if len(comb) == count:
        print(", ".join(comb))
        return

    for i in range(index, len(values)):
        comb.append(values[i])
        combinations(values, i + 1, count, comb)
        comb.pop()


index = 0
comb = []
names = input().split(", ")
n = int(input())
combinations(names, index, n, comb)
