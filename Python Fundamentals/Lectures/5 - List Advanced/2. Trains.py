wagons = int(input())
train_wagons = [0] * wagons

command = input()
while not command == "End":
    cmd = command.split()
    if cmd[0] == "add":
        train_wagons[-1] += int(cmd[1])
    elif cmd[0] == "insert":
        index = int(cmd[1])
        people = int(cmd[2])
        train_wagons[index] += people
    elif cmd[0] == "leave":
        index = int(cmd[1])
        people = int(cmd[2])
        train_wagons[index] -= people
    command = input()

print(train_wagons)

