class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        # while self.count > -1:
        #     value_to_return = self.count
        #     self.count -= 1
        #     return value_to_return
        # raise StopIteration
        if self.count < 0:
            raise StopIteration
        v_to_r = self.count
        self.count -= 1
        return v_to_r


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")



