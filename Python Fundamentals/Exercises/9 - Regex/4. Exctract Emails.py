import re

text = input()
pattern = r"\s(?P<email>(?P<user>[A-Za-z0-9]+[\-\.\_]*[A-Za-z0-9]*)@(?P<host>[A-Za-z]+[\w\-]*(\.[\w]+[\w\-]*)+))"

matched = re.finditer(pattern, text)

for match in matched:
    print(match.group('email'))

