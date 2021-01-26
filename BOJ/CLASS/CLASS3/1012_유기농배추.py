import sys

sys.setrecursionlimit(100000)

t = int(input())

answer = []
for _ in range(t):
    m, n, k = list(map(int, input().split()))
    graph = [[0]*m for _ in range(n)]

    def dfs(x, y):
        if x <= -1 or x >= m or y <= -1 or y >= n:
            return False
        if graph[y][x] == 1:
            graph[y][x] = 2
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
        return False

    for _ in range(k):
        x, y = list(map(int, input().split()))
        graph[y][x] = 1
    result = 0
    for x in range(m):
        for y in range(n):
            if dfs(x, y) == True:
                # print(graph)
                result += 1
    answer.append(result)

for i in answer:
    print(i)
