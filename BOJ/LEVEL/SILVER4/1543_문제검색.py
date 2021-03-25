import re
doc = input()

s = input()
p = re.compile(s)
result = p.findall(doc)

print(len(result))
