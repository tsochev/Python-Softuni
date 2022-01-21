def concatenate(*args):
    text = ""
    for el in args:
        text += el
    return text


print(concatenate("I", " ", "Love", " ", "Python"))