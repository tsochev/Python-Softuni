def squares(n):
    # for x in range(1, n + 1):
    #     yield x * x

    yield (x * x for x in range(1, n + 1))


print(list(squares(5)))