import re

pattern = r"(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
text = input()

matched = re.finditer(pattern, text)

print(", ".join([el.group() for el in matched]))
