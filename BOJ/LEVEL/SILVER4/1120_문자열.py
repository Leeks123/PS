x, y = input().split()


def sameStrCompare(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt


def getMinPosition(short, long):
    diff = len(long) - len(short)
    min = len(short)
    idx = 0
    for i in range(diff+1):
        tmp = sameStrCompare(short, long[i:i+len(short)])
        if tmp < min:
            min = tmp
            idx = i
    return min


print(getMinPosition(x, y))
