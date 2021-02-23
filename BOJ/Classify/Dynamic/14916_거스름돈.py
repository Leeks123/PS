n = int(input())

dp = [0, -1, 1, -1, 2, 1]


if n > 5:
    for x in range(6, n+1):
        an_1 = dp[x-2]+1
        an_2 = dp[x-5]+1
        if an_1 == 0:
            if an_2 != 0:
                dp.append(an_2)
                continue
            else:
                dp.append(-1)
                continue
        if an_2 == 0:
            if an_1 != 0:
                dp.append(an_1)
                continue
            else:
                dp.append(-1)
                continue
        dp.append(min(an_1, an_2))

print(dp[n])
