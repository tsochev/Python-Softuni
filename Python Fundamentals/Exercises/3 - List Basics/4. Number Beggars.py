string_of_integers = input().split(", ")
beggars = int(input())
sum_list = []

for num in string_of_integers:
    sum_list.append(int(num))

result_sum = [0] * beggars

for i in range(len(string_of_integers)):
        index = i % beggars
        result_sum[index] += sum_list[i]

print(result_sum)



