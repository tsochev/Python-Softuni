numbers = input().split(" ")

stack = []
reversed_nums = []
for el in numbers:
    stack.append(el)

while stack:
    reversed_nums.append(stack.pop())

print(" ".join(reversed_nums))