def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(sum_num, num_3):
    return sum_num - num_3


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(subtract(sum_numbers(number_1, number_2), number_3))
