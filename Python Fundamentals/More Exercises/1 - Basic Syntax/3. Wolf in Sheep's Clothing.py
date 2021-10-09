string = input().split(", ")
sheep_count = 0

if string[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(string)):
        if string[i] == "sheep":
            sheep_count += 1
        else:
            sheep_count = 0

    print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
