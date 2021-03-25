a, p = map(int, input().split())


def getNext(a, p):
    ret = 0
    i = a
    while True:
        # print(i)
        if i == 0:
            break
        ret += (i % 10)**p
        i = i//10
    return ret


d = [a]

while True:
    if getNext(d[-1], p) in d:
        d = d[:d.index(getNext(d[-1], p))]
        break
    d.append(getNext(d[-1], p))

# print(d)
print(len(d))
