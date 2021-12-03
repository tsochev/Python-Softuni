numbers = input(). split(" ")
numbers = [int(x) for x in numbers]
finish = len(numbers) // 2
left_d = numbers[0:finish]
right_d = numbers[:finish:-1]

left_driver = 0
right_driver = 0

for num in left_d:
    left_driver += num
    if num == 0:
        left_driver *= 0.8
for num_right in right_d:
    right_driver += num_right
    if num_right == 0:
        right_driver *= 0.8

if left_driver < right_driver:
    print(f"The winner is left with total time: {left_driver:.1f}")
else:
    print(f"The winner is right with total time: {right_driver:.1f}")
