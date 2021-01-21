n = int(input())
c = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(c):
    node = list(map(int, input().split()))
    graph[node[0]].append(node[1])
    graph[node[1]].append(node[0])

cnt = 0


def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False]*(n+1)

dfs(graph, 1, visited)

print(cnt-1)
