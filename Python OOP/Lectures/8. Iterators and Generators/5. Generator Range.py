def genrange(start, end):
    # for x in range(self.start, self.end + 1):
    #     yield x

    return (x for x in range(start, end + 1))


print(list(genrange(1, 10)))
