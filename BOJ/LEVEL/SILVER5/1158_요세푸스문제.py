from collections import deque

n, k = map(int, input().split())

q = deque([x for x in range(1, n+1)])

poped = []

while len(q) != 0:
    for _ in range(k-1):
        q.append(q.popleft())
    poped.append(q.popleft())

print('<', end='')
print(', '.join(map(str, poped)), end='>')
