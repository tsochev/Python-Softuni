n = int(input())

compounds = set()

for _ in range(n):
    elements = input().split()
    [compounds.add(g) for g in elements]

[print(g) for g in compounds]