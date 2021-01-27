from collections import deque

n, m, v = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    f, d = list(map(int, input().split()))
    graph[f].append(d)
    graph[d].append(f)
for i in range(n+1):
    graph[i].sort()

# print(graph)


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False]*(n+1)

dfs(graph, v, visited)
print()


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False]*(n+1)

bfs(graph, v, visited)
