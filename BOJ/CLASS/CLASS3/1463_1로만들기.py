n = int(input())

dp = [0, 0, 1, 1]


def makeOne(x):
    candidates = []
    if x % 2 == 0:
        candidates.append(dp[x//2]+1)
    if x % 3 == 0:
        candidates.append(dp[x//3]+1)
    candidates.append(dp[x-1]+1)
    return min(candidates)


if n <= 3:
    print(dp[n])
else:
    for i in range(4, n+1):
        dp.append(makeOne(i))
    print(dp[n])
