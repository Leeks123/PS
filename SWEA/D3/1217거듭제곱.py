
def pow(n, m):
    if m == 0:
        return 1
    else:
        return n*pow(n, m-1)


for _ in range(10):
    t = int(input())
    n, m = map(int, input().split())
    answer = pow(n, m)
    print('#'+str(t), answer)
