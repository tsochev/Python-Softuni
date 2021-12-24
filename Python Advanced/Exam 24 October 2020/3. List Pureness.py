from collections import deque
import sys


def best_list_pureness(list, k):
    sum_value = 0
    rotation = 0
    max_value = -sys.maxsize
    new_list = deque(list)
    for num in range(k + 1):
        sum_value = sum([(x * index) for x, index in enumerate(new_list)])
        if sum_value > max_value:
            max_value = sum_value
            rotation = num
        new_list.appendleft(new_list.pop())

    return f"Best pureness {sum_value} after {rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

