import re

pattern = r"(?P<Day>\d{2})(?P<sep>[-\./])(?P<Month>[A-Z][a-z]{2})(?P=sep)(?P<Year>\d{4})"
text = input()

matched = re.finditer(pattern, text)

for match in matched:
    curr_date = match.groupdict()
    print(f"Day: {curr_date['Day']}, Month: {curr_date['Month']}, Year: {curr_date['Year']}")
