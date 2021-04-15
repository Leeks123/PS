t = int(input())

for i in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    avg = sum(arr)/n
    cnt = 0
    for a in arr:
        if a <= avg:
            cnt += 1
    print('#'+str(i), cnt)
