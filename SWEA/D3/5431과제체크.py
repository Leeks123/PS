t = int(input())

for i in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    check = [False]*n
    for a in arr:
        check[a-1] = True

    print('#'+str(i), end=' ')
    for i in range(n):
        if check[i] == False:
            print(i+1, end=' ')
    print()
