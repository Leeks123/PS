
n = int(input())
posArr = list(map(int, input().split()))

uniqPosArr = list(set(posArr))
uniqPosArr.sort()  # O(nlogn)


def binarySearch(target, start, end, arr):
    mid = (start + end) // 2
    # print(target, arr[mid])
    if start > end:
        return False
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(target, start, mid-1, arr)
    else:
        return binarySearch(target, mid+1, end, arr)


answer = []
for i in posArr:
    answer.append(binarySearch(i, 0, len(uniqPosArr)-1, uniqPosArr))

for i in answer:
    print(i, end=' ')
