import re

pattern = r"\b\_(?P<variable_name>[A-Za-z0-9]+)\b"
variable_name = []
text = input()

matches = re.finditer(pattern, text)

for match in matches:
    variable_name.append(match.group('variable_name'))

print(",".join(variable_name))


