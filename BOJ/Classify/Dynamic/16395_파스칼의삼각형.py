n, k = map(int, input().split())

p = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j == 0:
            p[i][j] = 1
        elif j == i:
            p[i][j] = 1
        else:
            p[i][j] = p[i-1][j-1] + p[i-1][j]

print(p[n-1][k-1])
