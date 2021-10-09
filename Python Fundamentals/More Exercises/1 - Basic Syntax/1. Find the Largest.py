num = list(input())

for i in range(len(num) - 1):
    for x in range(i + 1, len(num)):
        if int(num[x]) > int(num[i]):
            current_num = int(num[i])
            num[i] = str(num[x])
            num[x] = str(current_num)

print("".join(num))