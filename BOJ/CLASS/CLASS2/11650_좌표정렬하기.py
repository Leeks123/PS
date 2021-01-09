n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr = sorted(arr, key=lambda p: p[1])
arr = sorted(arr, key=lambda p: p[0])

for i in arr:
    print(i[0], i[1])
