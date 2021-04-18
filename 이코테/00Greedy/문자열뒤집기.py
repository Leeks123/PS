import re

s = input()

z = re.compile('0+')
o = re.compile('1+')

zeros = len(z.findall(s))
ones = len(o.findall(s))

print(min(zeros, ones))
