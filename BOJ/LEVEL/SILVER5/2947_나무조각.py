arr = list(map(int, input().split()))

answer = [1, 2, 3, 4, 5]


def printArr(arr):
    for i in arr:
        print(i, end=' ')
    print()


while True:
    if arr == answer:
        break
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            printArr(arr)
