class custom_range_iterator:
    def __init__(self, custom_range):
        # self.custom_range = custom_range
        self.start = custom_range.start
        self.end = custom_range.end
        self.current_number = self.start

    def __next__(self):
        if self.current_number > self.end:
            raise StopIteration

        value_to_return = self.current_number
        self.current_number += 1
        return value_to_return


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current_number = self.start

    def __iter__(self):
        return custom_range_iterator(self)


# one_to_ten = custom_range(1, 10, 2)
# for num in one_to_ten:
#     print(num)


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)




# class custom_range_iterator:
#     def __init__(self, custom_range):
#         # self.custom_range = custom_range
#         self.start = custom_range.start
#         self.end = custom_range.end
#         self.step = custom_range.step
#         self.current_number = self.start
#
#     def __next__(self):
#         if self.step > 0 and self.current_number > self.end:
#             raise StopIteration
#         if self.step < 0 and self.current_number < self.end:
#             raise StopIteration
#
#         value_to_return = self.current_number
#         self.current_number += self.step
#         return value_to_return
#
#
# class custom_range:
#     def __init__(self, start, end, step=1):
#         self.start = start
#         self.end = end
#         self.step = step
#         self.current_number = self.start
#
#     def __iter__(self):
#         return custom_range_iterator(self)
#
#
# # one_to_ten = custom_range(1, 10, 2)
# # for num in one_to_ten:
# #     print(num)
#
#
# one_to_ten = custom_range(10, 1, -2)
# for num in one_to_ten:
#     print(num)
#
