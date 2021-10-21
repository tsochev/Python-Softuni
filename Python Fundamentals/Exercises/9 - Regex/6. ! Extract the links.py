import re

pattern = r"(?P<url>(?P<sub_domain>www)\.(?P<domain>[A-Za-z0-9]+(\-[A-Za-z0-9]+)*)(?P<domain_extension>(\.[a-z]+)+))"
# patterm = r"(?P<url>(?P<sub_domain>www)\.(?P<domain>[A-Za-z0-9]+(\-[A-Za-z0-9]+)*)(?P<domain_extension>(\.[a-z]+)+))"
valid_url = []

text = input()
while not text == "":
    matches = re.finditer(pattern, text)

    for match in matches:
        valid_url.append(match.group('url'))

    text = input()

for url in valid_url:
    print(url)