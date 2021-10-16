number = int(input())
synonyms = {}

for i in range(number):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word, synonym in synonyms.items():
    print(f"{word} - {', '.join(synonyms[word])}")
