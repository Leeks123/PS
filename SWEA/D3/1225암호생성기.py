def solve(arr):
    while True:
        for i in range(1, 6):
            arr[0] -= i
            arr = arr[1:]+arr[:1]
            if arr[-1] <= 0:
                arr[-1] = 0
                break
        if 0 in arr:
            break
    arr = list(map(str, arr))
    return ' '.join(arr)


for _ in range(10):
    t = int(input())
    arr = list(map(int, input().split()))
    answer = solve(arr)
    print('#'+str(t), answer)
