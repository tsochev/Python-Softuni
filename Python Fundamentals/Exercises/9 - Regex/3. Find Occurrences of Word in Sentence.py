import re

text = input()
searched_word = input()
pattern = rf"\b{searched_word}\b"

word_cont = len(re.findall(pattern, text, flags=re.IGNORECASE))

print(word_cont)

