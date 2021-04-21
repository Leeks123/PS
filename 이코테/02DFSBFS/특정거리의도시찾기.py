from collections import deque

n, m, distance, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)


def bfs(graph, start, visited, dist):
    q = deque([start])
    visited[start] = 0
    answer = []
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v]+1
                q.append(i)
                if visited[i] == dist:
                    answer.append(i)
    answer.sort()
    return answer


visited = [-1]*(n+1)
print(bfs(graph, start, visited, distance))
