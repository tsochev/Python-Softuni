from collections import deque

substrings = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

collected = []

while substrings:
    first = substrings.popleft()
    last = substrings.pop() if substrings else ""

    color = first + last
    if color in main_colors or color in secondary_colors:
        collected.append(color)
        continue
    color = last + first
    if color in main_colors or color in secondary_colors:
        collected.append(color)
    else:
        first = first[:-1]
        last = last[:-1]
        if first:
            substrings.insert(len(substrings) // 2, first)
        if last:
            substrings.insert(len(substrings) // 2, last)


secondary_required_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["blue", "yellow"],
}


for color in collected:
    if color in main_colors:
        continue
    required_colors = secondary_required_colors[color]
    is_valid = all([x in collected for x in required_colors])
    if not is_valid:
        collected.remove(color)

print(collected)
