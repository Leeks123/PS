n = int(input())
arr = list(map(int, input().split()))

s = list(set(arr))

s.sort()

for i in s:
    print(i, end=' ')
