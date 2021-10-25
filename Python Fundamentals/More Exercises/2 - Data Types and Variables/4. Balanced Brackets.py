lines = int(input())

open_bracket = 0
close_bracket = 0
is_balanced = True
for _ in range(1, lines + 1):
    symbol = input()
    if symbol == "(":
        open_bracket += 1
    if symbol == ")":
        close_bracket += 1

    if close_bracket > open_bracket:
        is_balanced = False
        break
    if open_bracket - 1 > close_bracket:
        is_balanced = False
        break
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
