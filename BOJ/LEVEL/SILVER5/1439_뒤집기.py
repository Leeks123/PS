import re

s = input()

regZero = re.compile('0+')
regOne = re.compile('1+')
zeros = len(re.findall(regZero, s))
ones = len(re.findall(regOne, s))

print(zeros if zeros < ones else ones)
