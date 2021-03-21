
import sys
n = int(input())

distances = list(map(int, sys.stdin.readline().rstrip().split()))
# distances.reverse()
prices = list(map(int, sys.stdin.readline().rstrip().split()))
prices.pop()
# prices.reverse()

# dp = [prices[0]*distances[0], ]

# for i in range(1, n-1):
#     dp.append(min(prices[i]*sum(distances[:i+1]),
#                   prices[i]*distances[i]+dp[i-1]))

# print(dp[-1])

answer = distances[0]*prices[0]
minPrice = prices[0]
for i in range(1, n-1):
    if minPrice > prices[i]:
        answer += distances[i]*prices[i]
        minPrice = prices[i]
    else:
        answer += distances[i]*minPrice

print(answer)
