n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

answer = (arr[-1]*3 + arr[-2]) * (m // 4) + (arr[-1]*(m % 4))

print(answer)
