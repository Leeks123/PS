from collections import deque

n, k = map(int, input().split())

visited = [0]*100001


def bfs(start, target):
    q = deque([start])
    visited[start] = 0
    while len(q) != 0:
        x = q.popleft()
        if x == target:
            break
        if x-1 >= 0:
            if visited[x-1] == 0:
                q.append(x-1)
                visited[x-1] = visited[x]+1
        if x+1 < 100001:
            if visited[x+1] == 0:
                q.append(x+1)
                visited[x+1] = visited[x]+1
        if 2*x < 100001:
            if visited[x*2] == 0:
                q.append(2*x)
                visited[2*x] = visited[x]+1


bfs(n, k)
print(visited[k])
