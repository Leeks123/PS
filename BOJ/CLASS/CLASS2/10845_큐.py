from sys import stdin
from collections import deque

n = int(input())
q = deque()

for i in range(n):
    s = stdin.readline().split()
    if s[0] == "push":
        q.append(int(s[1]))
    elif s[0] == "pop":
        print(q.popleft() if len(q) != 0 else -1)
    elif s[0] == "size":
        print(len(q))
    elif s[0] == "empty":
        print(1 if len(q) == 0 else 0)
    elif s[0] == "front":
        print(q[0] if len(q) != 0 else -1)
    elif s[0] == "back":
        print(q[-1] if len(q) != 0 else -1)
