n = int(input())

tri = []
dp = []
for i in range(n):
    floor = list(map(int, input().split()))
    tri.append(floor)
    if i > 0:
        dpFloor = []
        for j in range(len(floor)):
            if j == 0:
                dpFloor.append(dp[i-1][j]+floor[j])
            elif j == len(floor)-1:
                dpFloor.append(dp[i-1][j-1]+floor[j])
            else:
                dpFloor.append(max(dp[i-1][j]+floor[j], dp[i-1][j-1]+floor[j]))
        dp.append(dpFloor)
    else:
        dp.append(floor)

print(max(dp[-1]))
