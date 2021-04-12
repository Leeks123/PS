import sys
t = int(input())

for i in range(1, t + 1):
    l, u, x = map(int, sys.stdin.readline().split())
    if x > u:
        print('#'+str(i), -1)
    elif l < x < u:
        print('#'+str(i), 0)
    else:
        print('#'+str(i), l-x)
