t = int(input())

for i in range(1, t+1):
    n = int(input())
    print('#'+str(i), end=' ')
    for _ in range(n):
        print('1/'+str(n), end=' ')
    print()
