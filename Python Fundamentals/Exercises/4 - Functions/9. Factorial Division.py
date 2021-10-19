import math


def factorial_numbers(num_1: int, num_2: int):
    result = factorial_of_num_1(num_1) / factorial_of_num_2(num_2)
    return f"{result:.2f}"


def factorial_of_num_1(num_1: int):
    return math.factorial(num_1)


def factorial_of_num_2(num_2: int):
    return math.factorial(num_2)


number_1 = int(input())
number_2 = int(input())
print(factorial_numbers(number_1, number_2))
