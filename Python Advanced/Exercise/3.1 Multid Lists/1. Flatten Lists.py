sublists = input().split("|")

result = []

for index in range(len(sublists) - 1, - 1, -1):
    el = sublists[index].split()
    result += el

print(" ".join(result))
