from collections import deque

queue = deque()

while True:
    command = input()
    if command == "End":
        break
    elif command == "Paid":
        while queue:
            print(queue.pop())
    else:
        queue.appendleft(command)

print(f"{len(queue)} people remaining.")