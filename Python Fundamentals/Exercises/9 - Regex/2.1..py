import re

text = input()
pattern = r'\b\_(?P<variable_name>[A-Za-z0-9]+)\b'

print(','.join([match.group('variable_name') for match in re.finditer(pattern, text)]))