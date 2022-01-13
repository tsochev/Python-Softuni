def is_there_knight(board, row, col):
    board_size = len(board)
    if row < 0 or col < 0 or row >= board_size or col >= board_size:
        return False
    return board[row][col] == "K"


def get_affected_knights(board, row, col):
    result = 0
    if is_there_knight(board, row - 2, col - 1):
        result += 1
    if is_there_knight(board, row - 1, col - 2):
        result += 1
    if is_there_knight(board, row - 2, col + 1):
        result += 1
    if is_there_knight(board, row - 1, col + 2):
        result += 1
    if is_there_knight(board, row + 1, col - 2):
        result += 1
    if is_there_knight(board, row + 2, col - 1):
        result += 1
    if is_there_knight(board, row + 1, col + 2):
        result += 1
    if is_there_knight(board, row + 2, col + 1):
        result += 1
    return result


size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0

while True:
    max_count = 0
    knight_row = 0
    knight_col = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "0":
                continue

            count = get_affected_knights(matrix, r, c)
            if count > max_count:
                max_count, knight_row, knight_col = count, r, c

    if max_count == 0:
        break
    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)
