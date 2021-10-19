def sum_or_even(num):
    odd_sum = 0
    even_sum = 0

    for n in num:
        n = int(n)
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(sum_or_even(number))
