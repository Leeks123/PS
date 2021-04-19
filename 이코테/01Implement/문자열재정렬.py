s = input()

alp = []
num = 0

for i in range(len(s)):
    if s[i].isdigit():
        num += int(s[i])
    else:
        alp.append(s[i])

alp.sort()
print(''.join(alp), end='')
print(num)
