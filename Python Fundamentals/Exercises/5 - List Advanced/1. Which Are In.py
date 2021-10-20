searched_words = input().split(", ")
given_words = input().split(", ")
new_list = []
for el in searched_words:
    for word in given_words:
        if word.find(el) > -1:
            new_list.append(el)
            break
print(new_list)