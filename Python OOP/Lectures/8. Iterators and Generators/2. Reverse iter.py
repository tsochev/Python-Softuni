class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.idx) > len(self.iterable):
            raise StopIteration
        value_to_return = self.iterable[self.idx]
        self.idx -= 1
        return value_to_return


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
