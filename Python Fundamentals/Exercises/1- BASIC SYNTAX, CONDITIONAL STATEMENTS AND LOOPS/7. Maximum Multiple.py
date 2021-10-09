divisor = int(input())
bound = int(input())
max_multiplier = 0
for num in range(divisor + 1, bound + 1):
    if num % divisor == 0:
        max_multiplier = num
print(max_multiplier)