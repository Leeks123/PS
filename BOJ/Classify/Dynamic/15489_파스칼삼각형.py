r, c, w = map(int, input().split())

p = [[0]*(r+w) for _ in range(r+w)]

for i in range(r+w):
    for j in range(r+w):
        if j == 0:
            p[i][j] = 1
        elif j == i:
            p[i][j] = 1
        else:
            p[i][j] = p[i-1][j-1] + p[i-1][j]

answer = 0
for i in range(r-1, r-1+w):
    for j in range(c-1, c+1+i-r):
        # print(p[i][j], i, j)
        answer += p[i][j]
print(answer)
