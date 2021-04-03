n = int(input())
m = int(input())

arr = list(map(int, input().split()))

answer = 0

while len(arr) != 0:
    target = arr[0]
    arr = arr[1:]
    if m-target in arr:
        del arr[arr.index(m-target)]
        answer += 1

print(answer)
