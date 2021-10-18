factor = int(input())
count = int(input())

my_list = []

for el in range(1, count + 1):
    result = factor * el
    my_list.append(result)
print(my_list)