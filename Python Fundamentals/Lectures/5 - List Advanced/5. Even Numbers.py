numbers = [int(el) for el in input().split(", ")]
print([i for i in range(len(numbers)) if numbers[i] % 2 == 0])

# print([i for el in numbers if el % 2 == 0])
