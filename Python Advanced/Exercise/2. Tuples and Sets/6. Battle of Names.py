n = int(input())

even = set()
odd = set()

for row in range(1, n + 1):
    sum_name = sum([ord(x) for x in input()]) // row
    if sum_name % 2 == 0:
        even.add(sum_name)
    else:
        odd.add(sum_name)

even_sum = sum(even)
odd_sum = sum(odd)

result = set()
if even_sum == odd_sum:
    result = odd.union(even)
elif even_sum < odd_sum:
    result = odd.difference(even)
else:
    result = odd.symmetric_difference(even)

print(', '.join([str(x) for x in result]))