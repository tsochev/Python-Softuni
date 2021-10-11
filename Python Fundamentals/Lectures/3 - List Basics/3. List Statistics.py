num = int(input())

positive_num = []
negative_num = []

for _ in range(num):
    current_num = int(input())
    if current_num >= 0:
        positive_num.append(current_num)
    else:
        negative_num.append(current_num)

print(positive_num)
print(negative_num)
print(f"Count of positives: {len(positive_num)}. Sum of negatives: {sum(negative_num)}")
