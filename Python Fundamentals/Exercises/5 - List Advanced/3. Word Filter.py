words = [el for el in input().split()]

new_words = [print(el) for el in words if len(el) % 2 == 0]