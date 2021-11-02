class ValueCannotBeNegative(Exception):
    pass


numbers = [int(input()) for x in range(5)]

for number in numbers:
    if number < 0:
        raise ValueCannotBeNegative

