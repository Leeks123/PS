import heapq
import sys

n = sys.stdin.readline().rstrip()
h = []
for _ in range(int(n)):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (-1*x, x))
