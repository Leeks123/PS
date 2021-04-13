t = int(input())


def solve(n):
    h = n//30
    m = (n % 30)*2
    return h, m


for i in range(1, t+1):
    deg = int(input())
    hour, min = solve(deg)
    print('#'+str(i), hour, min)
