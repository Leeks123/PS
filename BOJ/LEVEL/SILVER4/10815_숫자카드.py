n = int(input())

cards = list(map(int, input().split()))

m = int(input())

willFind = list(map(int, input().split()))

cards.sort()


def binarySearch(arr, target, start, end):
    mid = (start+end) // 2
    # print('-------------')
    # print(start, mid, end)
    if start > end:
        return None
    if arr[mid] == target:
        return mid
    else:
        if arr[mid] > target:
            return binarySearch(arr, target, start, mid-1)
        else:
            return binarySearch(arr, target, mid+1, end)


for i in willFind:
    print(0 if binarySearch(cards, i, 0, len(cards)-1) is None else 1, end=' ')
