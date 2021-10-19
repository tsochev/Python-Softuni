def perfect_num(num: int):
    sum_divisors = 0
    for n in range(1, num):
        if num % n == 0:
            sum_divisors += n
    if sum_divisors == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_num(number))