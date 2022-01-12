rows, cols = [int(x) for x in input().split()]
word = input()

matrix = []
word_index = 0

for row in range(rows):
    matrix.append([None] * cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = word[word_index]
        else:
            matrix[row][cols - 1 - col] = word[word_index]
        word_index = (word_index + 1) % len(word)

for row in matrix:
    print(''.join(row))