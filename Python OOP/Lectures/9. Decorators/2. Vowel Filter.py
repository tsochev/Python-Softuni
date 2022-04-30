import functools


def is_vowel(ch):
    return ch in "aeiouy"


def vowel_filter(func):
    @functools.wraps(func)
    def wrapper():
        result = func()

        return [x for x in result if is_vowel(x)]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
