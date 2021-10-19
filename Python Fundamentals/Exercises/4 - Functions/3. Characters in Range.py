def string(t_1, t_2):
    char = ord(t_1)
    char_2 = ord(t_2)
    for sym in range(char + 1, char_2):
        sym = chr(sym)
        my_list.append(sym)

    return my_list


my_list = []
symbol_1 = input()
symbol_2 = input()
print(" ".join(string(symbol_1, symbol_2)))
