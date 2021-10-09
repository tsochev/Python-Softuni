num_of_lines = int(input())
result = 0
for symbol in range(1, num_of_lines + 1):
    letter = input()
    result += ord(letter)
print(f"The sum equals: {result}")
