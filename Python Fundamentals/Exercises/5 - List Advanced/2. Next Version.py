current_version = [int(x) for x in input().split(".")]

for i in range(len(current_version) - 1, - 1, - 1):
    if not current_version[i] == 9:
        current_version[i] += 1
        break
    else:
        current_version[i] = 0
print(*current_version, sep=".")
