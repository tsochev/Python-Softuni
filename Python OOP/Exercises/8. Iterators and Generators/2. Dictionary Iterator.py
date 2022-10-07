class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.index_keys = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_keys >= len(self.keys):
            raise StopIteration
        key = self.keys[self.index_keys]
        value = self.dictionary[key]
        self.index_keys += 1
        return key, value


# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
