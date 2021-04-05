INF = int(1e9)
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = [[INF]*(n) for _ in range(n)]

for a in range(0, n):
    for b in range(0, n):
        if graph[a][b] == 1:
            answer[a][b] = 1


for k in range(0, n):
    for a in range(0, n):
        for b in range(0, n):
            answer[a][b] = min(answer[a][b], answer[a][k]+answer[k][b])

for a in range(n):
    for b in range(n):
        if answer[a][b] == INF:
            answer[a][b] = 0
        else:
            answer[a][b] = 1

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()
