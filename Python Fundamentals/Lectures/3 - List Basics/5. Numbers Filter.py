number = int(input())

even = []
odd = []
negative = []
positive = []

for _ in range(number):
    integer = int(input())
    if integer >= 0:
        positive.append(integer)
    if integer % 2 == 0:
        even.append(integer)
    if integer % 2 == 1:
        odd.append(integer)
    if integer < 0:
        negative.append(integer)

command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
elif command == "positive":
    print(positive)