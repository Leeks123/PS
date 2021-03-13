a, b = map(int, input().split())

m = int(input())

baseA = list(map(int, input().split()))
baseA.reverse()


def AtoDec(baseA, m, a):
    ret = 0
    for i in range(m):
        ret += a**i*baseA[i]
    return ret


def DectoB(dec, b):
    ret = []
    while True:
        if dec < b:
            ret.append(dec)
            break
        ret.append(dec % b)
        dec = dec // b
    ret.reverse()
    return ret


# print(a)
dec = AtoDec(baseA, m, a)
# print(dec)
answer = DectoB(dec, b)

for a in answer:
    print(a, end=' ')
