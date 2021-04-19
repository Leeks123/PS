n = int(input())

cnt = 0


def includes3(arr):
    s = list(map(str, arr))
    s = ''.join(s)
    if '3' in s:
        return True
    return False


for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if includes3([h, m, s]):
                cnt += 1

print(cnt)
