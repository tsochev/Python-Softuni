import re

pattern = r"(?P<nums>[0-9]+)"
nums = []
text = input()
while not text == "":

    matches = re.findall(pattern, text)
    for match in matches:
        nums.append(match)

    text = input()

print(" ".join(nums))