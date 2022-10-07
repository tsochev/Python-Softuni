class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        # if self.number == 0:
        #     raise StopIteration
        # v_to_r = self.sequence[self.idx]
        # self.number -= 1
        # self.idx += 1
        # if self.idx == len(self.sequence):
        #     self.idx = 0
        #
        # return v_to_r

        if self.idx >= self.number:
            raise StopIteration
        v_to_r = self.sequence[self.idx % len(self.sequence)]
        self.idx += 1
        return v_to_r


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
