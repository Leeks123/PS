n, k = map(int, input().split())

arr = [x for x in range(1, n+1)]
ret = []
currentIdx = 0

while True:
    if len(arr) == 0:
        break
    currentIdx = (currentIdx+k-1) % len(arr)
    ret.append(arr[currentIdx])
    del arr[currentIdx]
    # print(arr)

answer = "<"
for s in ret:
    answer += str(s)+", "
answer = answer[:-2]+">"
print(answer)
