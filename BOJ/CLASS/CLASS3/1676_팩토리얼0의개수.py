import math

n = int(input())

s = list(str(math.factorial(n)))
s.reverse()

cnt = 0
for i in range(len(s)):
    if s[i] == '0':
        cnt += 1
    else:
        break

print(cnt)
