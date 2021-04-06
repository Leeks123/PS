import sys
n, m = map(int, input().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
prefix_sum = [0, ]
sum = 0
for i in arr:
    sum += i
    prefix_sum.append(sum)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[b]-prefix_sum[a-1])
