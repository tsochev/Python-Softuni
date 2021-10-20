numbers = [int(el) for el in input().split(", ")]

positive = [str(el) for el in numbers if el >= 0]
negative = [str(el) for el in numbers if el < 0]
even = [str(el) for el in numbers if el % 2 == 0]
odd = [str(el) for el in numbers if not el % 2 == 0]

print("Positive: " + ", ".join(positive))
print("Negative: " + ", ".join(negative))
print("Even: " + ", ".join(even))
print("Odd: " + ", ".join(odd))