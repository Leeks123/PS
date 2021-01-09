n = int(input())

arr = [x for x in range(1, n+1)]


while True:
    t = len(arr)
    if t == 1:
        print(arr[0])
        break
    arr = arr[1::2]
    if t % 2 == 1:
        arr.append(arr[0])
        arr = arr[1:]
