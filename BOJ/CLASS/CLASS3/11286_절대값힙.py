import sys
import heapq
n = int(input())

heap = []

for _ in range(n):
    i = int(sys.stdin.readline())
    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, ((abs(i), i)))
