n, m = map(int, input().split())

l = []
for _ in range(n):
    l.append(input())
l = set(l)

s = []
for _ in range(m):
    s.append(input())
s = set(s)

ret = list(s & l)
ret.sort()
print(len(ret))
for i in ret:
    print(i)
