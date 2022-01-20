command = input()
nums = [int(x) for x in input().split()]

if command == "Odd":
    odd = sum([x for x in nums if x % 2 != 0])
    result = odd * len(nums)
    print(result)
else:
    even = sum([x for x in nums if x % 2 == 0])
    result = even * len(nums)
    print(result)

# parity = 0 if command == "Even" else 1
# filter_sum = sum(filter(lambda x: x % 2 == parity, nums))
# print(filter_sum * len(nums))
