n = int(input())

title = []
i = 666

while len(title) < n:
    s = str(i)
    if '666' in s:
        title.append(i)
    i += 1

print(title[n-1])
