string = input().split(", ")
numbers = []
zero_list = []
for num in string:
    numbers.append(int(num))
    if int(num) == 0:
        numbers.remove(int(num))
        zero_list.append(int(num))
numbers += zero_list

print(numbers)