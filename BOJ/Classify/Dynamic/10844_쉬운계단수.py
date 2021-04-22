n = int(input())

dp = [0, 9]
counter = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n+1):
    dp.append(dp[i-1]*2 - (counter[0]+counter[9]))

    nextCounter = [0]*10
    for j in range(len(counter)):
        if j == 0 and counter[j] != 0:
            nextCounter[j+1] += counter[j]
        elif j == 9 and counter[j] != 0:
            nextCounter[j-1] += counter[j]
        else:
            if counter[j] != 0:
                nextCounter[j+1] += counter[j]
                nextCounter[j-1] += counter[j]
    for j in range(10):
        counter[j] = nextCounter[j]

print(dp[-1] % 1000000000)
