n = int(input())

wines = [int(input()) for _ in range(n)]

dp = []

for i in range(n):
    if i == 0:
        dp.append(wines[0])
    elif i == 1:
        dp.append(dp[0]+wines[1])
    elif i == 2:
        dp.append(max(max(wines[0], wines[1])+wines[2], dp[1]))
    else:
        dp.append(max(max(dp[i-2], dp[i-3]+wines[i-1])+wines[i], dp[i-1]))

# print(dp)
print(max(dp))
