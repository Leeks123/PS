
n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = 0


def dfs(graph, v, visited, cnt, target):
    global answer
    visited[v] = True
    # print(v, target, cnt, visited)
    if v == target:
        answer = cnt
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, cnt+1, target)


visited = [False]*(n+1)

dfs(graph, a, visited, 0, b)

print(answer if answer != 0 else -1)
