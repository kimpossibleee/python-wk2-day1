import re

with open('day1/hw/regex_test.txt', 'r') as file:
    contents = file.readlines()
    print(contents)

pattern = re.compile(r'([A-Z][a-z]+)(\s(([A-Z][a-z]+)|[A-Z]))?(\s[A-Z][a-z]+)')

for name in contents:
    name = name.strip('\n')
    # print(name)
    match = pattern.match(name)
    print(match.group(0) if match else None)
