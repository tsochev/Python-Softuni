class vowels:
    vowels_letter = "AEIOUYaeiouy"

    def __init__(self, text):
        self.text = text
        self. idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        # while self.idx < len(self.text):
        #     if self.text[self.idx] in self.vowels_letter:
        #         value_to_return = self.text[self.idx]
        #         self.idx += 1
        #         return value_to_return
        #     self.idx += 1
        # raise StopIteration

        while self.idx < len(self.text) and self.text[self.idx] not in self.vowels_letter:
            self.idx += 1

        if self.idx == len(self.text):
            raise StopIteration

        value_to_return = self.text[self.idx]
        self.idx += 1
        return value_to_return


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
