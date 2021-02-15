import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)


def dfs(graph, v, visited):
    visited[v] += 1
    print("dfs :", v)
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)


visited = [0]*(n+1)

cnt = 0
for i in range(1, n+1):
    if visited[i] == 0:
        dfs(graph, i, visited)
        cnt += 1
        print('cnt :', cnt)

print(cnt)
