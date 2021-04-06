from sys import stdin

n, m = map(int, input().split())

pocketmons = {}
for i in range(n):
    s = stdin.readline().rstrip()
    pocketmons[str(i+1)] = s
    pocketmons[s] = i+1


for i in range(m):
    q = stdin.readline().rstrip()
    print(pocketmons[q])
