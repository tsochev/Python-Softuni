def reverse_text(string):
    index = -1
    while abs(index) < len(string) + 1:
        yield string[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')
