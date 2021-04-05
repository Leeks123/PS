from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(n+1):
    graph[i].sort()


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[v]+1


answer = []
for i in range(1, n+1):
    visited = [0]*(n+1)
    bfs(graph, i, visited)
    answer.append(sum(visited) - visited[i])

print(answer.index(min(answer))+1)
