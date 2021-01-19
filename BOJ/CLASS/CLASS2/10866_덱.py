from sys import stdin
from collections import deque

n = int(input())
dq = deque()


for i in range(n):
    s = stdin.readline().split()
    if s[0] == "push_front":
        dq.appendleft(int(s[1]))
    elif s[0] == "push_back":
        dq.append(int(s[1]))
    elif s[0] == "pop_front":
        print(dq.popleft() if len(dq) != 0 else -1)
    elif s[0] == "pop_back":
        print(dq.pop() if len(dq) != 0 else -1)
    elif s[0] == "size":
        print(len(dq))
    elif s[0] == "empty":
        print(1 if len(dq) == 0 else 0)
    elif s[0] == "front":
        print(dq[0] if len(dq) != 0 else -1)
    elif s[0] == "back":
        print(dq[-1] if len(dq) != 0 else -1)
