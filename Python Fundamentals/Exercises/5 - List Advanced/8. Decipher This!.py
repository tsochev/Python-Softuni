def num_to_chr(word: str):
    num_as_str = ""
    new_word = []

    for ch in word:
        if ch.isnumeric():
            num_as_str += ch
        else:
            new_word.append(ch)

    chr_at_beginning = chr(int(num_as_str))
    new_word.insert(0, chr_at_beginning)

    return new_word


def decipher_word(word: str):
    new_word = num_to_chr(word)

    new_word[1], new_word[-1] = new_word[-1], new_word[1]

    return "".join(new_word)


words = input().split()

deciphered_words = [decipher_word(word) for word in words]

print(" ".join(deciphered_words))