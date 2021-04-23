n = int(input())

cards = list(map(int, input().split()))

dp = [0]

for i in range(1, n+1):
    if i == 1:
        dp.append(cards[i-1])
    elif i == 2:
        dp.append(max(cards[i-1], dp[i-1]*2))
    else:
        candidates = [cards[i-1]]
        for j in range(1, i):
            candidates.append(dp[i-j]+dp[j])
        dp.append(max(candidates))

print(max(dp))
