def find_sum(numbers_list):
    # lists = [int(x) for x in input().split(", ")]
    result = 1
    numbers_list_count = len(numbers_list)

    for i in range(numbers_list_count):
        number = numbers_list[i]
        if number <= 5:
            result *= number
        elif number <= 10:
            result /= number
    return result


print(find_sum([1, 4, 5]))
print(find_sum([4, 5, 6, 1, 3]))
print(find_sum([2, 5, 10]))
