from collections import deque

n = int(input())

board = []
lowest = 101
highest = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    lowest = min(arr) if min(arr) < lowest else lowest
    highest = max(arr) if max(arr) > highest else highest
    board.append(arr)


def bfs(graph, start, flood):
    q = deque([start])

    if graph[start[0]][start[1]] <= flood:
        return 0
    else:
        graph[start[0]][start[1]] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        v = q.popleft()

        for i in range(4):
            nx = v[0]+dx[i]
            ny = v[1]+dy[i]

            if nx >= 0 and nx < len(graph) and ny >= 0 and ny < len(graph):
                if graph[nx][ny] > flood:
                    q.append((nx, ny))
                    graph[nx][ny] = 0
    return 1


candidates = []
for fl in range(lowest-1, highest+1):
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = board[i][j]

    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += bfs(temp, (i, j), fl)

    candidates.append(cnt)

print(max(candidates))
