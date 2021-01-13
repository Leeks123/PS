k, n = map(int, input().split())

cables = []
for _ in range(k):
    cables.append(int(input()))


def cuttedCounter(cables, l):
    ret = 0
    for i in cables:
        ret += i//l
    return ret


end = max(cables)
start = 1
answer = 0
while start <= end:
    m = (start+end)//2
    # print(start, end, m)
    if cuttedCounter(cables, m) >= n:
        if m == answer:
            break
        answer = m if answer < m else answer
        start = m+1
    else:
        end = m-1


print(answer)
