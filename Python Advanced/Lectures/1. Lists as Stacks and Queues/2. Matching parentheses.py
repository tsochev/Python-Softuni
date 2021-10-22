string = input()

stack = []

for index, n in enumerate(string):
    if n == "(":
        stack.append(index)
    elif n == ")":
        closed_index = index
        opening_index = stack.pop()
        print(string[opening_index: closed_index + 1])