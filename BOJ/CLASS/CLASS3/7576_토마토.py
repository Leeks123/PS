from collections import deque
m, n = map(int, input().split())

box = []

for _ in range(n):
    box.append(list(map(int, input().split())))

starts = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            starts.append((i, j))


def bfs(starts, graph):
    q = deque(starts)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while len(q) != 0:
        node = q.popleft()

        for i in range(4):
            if dx[i]+node[0] >= 0 and dx[i]+node[0] < n and dy[i]+node[1] >= 0 and dy[i]+node[1] < m:  # 미로 내부
                x = dx[i]+node[0]
                y = dy[i]+node[1]
                if graph[x][y] == 0:  # 방문한적 없음
                    # print('방문가능:', x, y)
                    q.append((x, y))
                    graph[x][y] = graph[node[0]][node[1]]+1  # 방문 체크


bfs(starts, box)


def answer():
    ret = 0
    for row in box:
        if 0 in row:
            return -1
        if max(row) > ret:
            ret = max(row)
    return ret-1


print(answer())
