numbers = input().split(" ")
text = input()
text = [x for x in text]
message = []
the_text = len(text)
for symbol in numbers:
    char = [int(x) for x in symbol]
    if len(text) < sum(char)+1:
        index = sum(char) - len(text)
    else:
        index = sum(char)
    message.append(text[index])
    text.pop(index)
print("".join(message))