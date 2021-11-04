def permute(index, value):
    if index == len(value):
        print("".join(value))
        return
    for i in range(index, len(value)):
        value[i], value[index] = value[index], value[i]
        permute(index + 1, value)
        value[i], value[index] = value[index], value[i]


text = input()
permute(0, list(text))

