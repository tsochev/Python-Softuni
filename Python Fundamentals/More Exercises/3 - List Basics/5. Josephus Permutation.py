first_list = input().split(" ")
first_list = [int(x) for x in first_list]
k = int(input())
new_list = []
count = 0
index = 0


while len(first_list) > 0:
    count += 1
    if count % k == 0:
        new_list.append((first_list.pop(index)))
    else:
        index += 1
    if index >= len(first_list):
        index = 0

print(new_list)
