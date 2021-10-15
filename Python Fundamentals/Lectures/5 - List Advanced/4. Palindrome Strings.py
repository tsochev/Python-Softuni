words = input().split()
palindrome = input()
found_palindrome = [el for el in words if el == el[::-1]]

print(found_palindrome)
print(f"Found palindrome {found_palindrome.count(palindrome)} times")