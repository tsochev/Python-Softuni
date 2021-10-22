string = input()

stack = []

for ch in string:
    stack.append(ch)

result = ""

while len(stack) > 0:
    result += stack.pop()

print(result)