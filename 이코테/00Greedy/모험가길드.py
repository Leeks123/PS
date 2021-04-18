n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

cnt = 0
while len(arr) != 0:
    if arr[0] > len(arr):
        break
    print(arr)
    arr = arr[arr[0]:]
    cnt += 1

print(cnt)
