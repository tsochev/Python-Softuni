import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()

matched = re.finditer(pattern, text)
matched = [num.group() for num in matched]
print(*matched)