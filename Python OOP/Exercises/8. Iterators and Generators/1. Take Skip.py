class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.curr_idx = 0
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.curr_idx < self.count:
            value_to_return = self.number
            self.number += self.step
            self.curr_idx += 1
            return value_to_return
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
