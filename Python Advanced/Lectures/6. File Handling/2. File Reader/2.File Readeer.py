file = open("numbers.txt")

sum = 0
for line in file:
    sum += int(line)

print(sum)
