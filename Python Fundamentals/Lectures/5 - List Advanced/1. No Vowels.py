text = input()
vowels = ["a", "o", "u", "e", "i"]
no_vowels = [el for el in text if not el in vowels]

print("".join(no_vowels))