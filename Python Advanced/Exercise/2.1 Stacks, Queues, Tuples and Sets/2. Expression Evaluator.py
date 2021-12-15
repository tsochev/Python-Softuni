from collections import deque

arithmetic_expressions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

expression = input().split()

numbers = deque()

for el in expression:
    if el in arithmetic_expressions:
        result = numbers.popleft()
        while numbers:
            number = numbers.popleft()
            result = arithmetic_expressions[el](result, number)
        numbers.append(result)
    else:
        numbers.append(int(el))

print(numbers.popleft())