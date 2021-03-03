# 메모리 초과
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False]*(n+1)

visitCnt = [0]*(n+1)

for i in range(1, n+1):
    dfs(graph, i, visited)
    visitCnt[i] = visited.count(True)
    visited = [False]*(n+1)

maxValue = max(visitCnt)
for i in range(len(visitCnt)):
    if visitCnt[i] == maxValue:
        print(i, end=' ')
