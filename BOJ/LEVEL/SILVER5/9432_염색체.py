import re
t = int(input())


def check(s):
    p = re.compile('^[ABCDEF]?A+F+C+[ABCDEF]?$')
    if p.match(s):
        return 'Infected!'
    else:
        return 'Good'


answers = []
for _ in range(t):
    s = input()
    answers.append(check(s))

for a in answers:
    print(a)
