def check_if_palindrome(el):
    if el == el[::-1]:
        return True
    return False


nums_as_str = input().split(", ")

for num_as_str in nums_as_str:
    print(check_if_palindrome(num_as_str))