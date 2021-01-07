n, m = map(int, input().split())


def getGCD(n, m):
    a = n if n > m else m
    b = m if n > m else n
    if a % b == 0:
        return b
    else:
        return getGCD(b, a % b)


def getLCM(n, m):
    a = n if n > m else m
    b = m if n > m else n
    gcd = getGCD(a, b)
    return int(a*b/gcd)


print(getGCD(n, m))
print(getLCM(n, m))
