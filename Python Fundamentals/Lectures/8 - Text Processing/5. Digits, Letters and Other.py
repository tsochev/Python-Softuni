word = input()

digits = ""
letters = ""
other = ""

for el in word:
    if el.isdigit():
        digits += el
    elif el.isalpha():
        letters += el
    else:
        other += el

print(digits)
print(letters)
print(other)