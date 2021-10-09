num = input()
number = ""

while True:
    number += max(num)
    num = num.replace(max(num), '', 1)
    if num == "":
        break
print(int(number))