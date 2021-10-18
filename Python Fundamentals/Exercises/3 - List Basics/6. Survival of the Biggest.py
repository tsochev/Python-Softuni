str_of_num = input().split()
n_removes = int(input())

for n in range(len(str_of_num)):
    str_of_num[n] = int(str_of_num[n])

for i in range(n_removes):
    min_element = min(str_of_num)
    str_of_num.remove(min_element)
for n in range(len(str_of_num)):
    str_of_num[n] = str(str_of_num[n])

print(", ".join(str_of_num))
