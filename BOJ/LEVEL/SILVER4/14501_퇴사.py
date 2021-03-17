n = int(input())

arr = []
for _ in range(n):
    t, p = map(int, input().split())
    arr.append((t, p))

arr.reverse()
dp = [arr[0][1] if arr[0][0] == 1 else 0, ]

for i in range(1, len(arr)):
    # print(i, '----------')
    if arr[i][0] > i+1:  # 남은 일수보다 상담일이 크다
        # print('check', arr[i][0])
        dp.append(dp[i-1])
    elif arr[i][0] == i+1:
        # print('남은 일수랑 상담일이 같음')
        dp.append(max(arr[i][1], dp[i-1]))
    else:
        # print('max', arr[i][1] + dp[i - arr[i][0]], dp[i-1])
        dp.append(max(arr[i][1] + dp[i - arr[i][0]], dp[i-1]))

print(dp[-1])
