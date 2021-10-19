def small_int(num_1, num_2, num_3):
    smallest = 0
    if num_1 < num_2 and num_1 < num_3:
        smallest = num_1
    if num_2 < num_3 and num_2 < num_1:
        smallest = num_2
    if num_3 < num_1 and num_3 < num_2:
        smallest = num_3
    return smallest


n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
print(small_int(n_1, n_2, n_3))