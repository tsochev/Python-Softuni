gifts = input().split()
command = input()

while not command == "No Money":
    command_split = command.split()
    if command_split[0] == "OutOfStock":
        for i in range(len(gifts)):
            if command_split[1] == gifts[i]:
                gifts[i] = "None"

    elif command_split[0] == "Required":
        command_index = int(command_split[2])
        if 0 <= command_index < len(gifts):
            gifts[command_index] = command_split[1]

    elif command_split[0] == "JustInCase":
        gifts[-1] = command_split[1]

    command = input()

count_of_none = gifts.count("None")
for _ in range(count_of_none):
    gifts.remove("None")
print(" ".join(gifts))
# print(" ".join([item for item in gifts if item != "None"]))
