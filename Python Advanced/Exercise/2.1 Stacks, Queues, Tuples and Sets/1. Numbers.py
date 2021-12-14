first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    text = input().split()
    command = text[0]
    position = text[1]

    if command == "Add" and position == "First":
        [first.add(int(x)) for x in text[2:]]
    elif command == "Add" and position == "Second":
        [second.add(int(x)) for x in text[2:]]
    elif command == "Remove" and position == "First":
        current_set = set([int(x) for x in text[2:]])
        first = first.difference(current_set)
    elif command == "Remove" and position == "Second":
        current_set = set([int(x) for x in text[2:]])
        second = second.difference(current_set)
    else:
        print(first.issubset(second) or second.issubset(first))

print(", ".join([str(x) for x in sorted(first)]))
print(", ".join([str(x) for x in sorted(second)]))
