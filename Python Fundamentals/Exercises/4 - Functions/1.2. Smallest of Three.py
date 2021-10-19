def small_int(num_1):
    min_int = min(num_1)
    return min_int


my_list = list(input())
my_list_int = [int(x) for x in my_list]
print(small_int(my_list_int))
