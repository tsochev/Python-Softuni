pours = int(input())
result = 0
total_liters = 255

for turn in range(1, pours + 1):
    pour_liters = int(input())
    result += pour_liters
    if total_liters < result:
        print("Insufficient capacity!")
        result -= pour_liters
print(result)

