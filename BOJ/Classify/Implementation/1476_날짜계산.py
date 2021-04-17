e, s, m = map(int, input().split())

n = 15*28*19


def subX(n, i):
    a = 0
    while True:
        if ((n/i)*a) % i == 1:
            break
        a += 1
    return a


div = ((n/15)*e*subX(n, 15) + (n/28)*s*subX(n, 28) + (n/19)*m*subX(n, 19)) // n
mod = ((n/15)*e*subX(n, 15) + (n/28)*s*subX(n, 28) + (n/19)*m*subX(n, 19)) % n
x = n + mod if mod == 0 else mod
print(int(x))
