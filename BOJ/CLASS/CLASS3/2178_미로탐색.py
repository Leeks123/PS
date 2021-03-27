from collections import deque

n, m = map(int, input().split())

maze = []
for _ in range(n):
    arr = list(map(int, list(input())))
    maze.append(arr)


def bfs(start, graph, target):
    q = deque([start])
    graph[start[0]][start[1]] = -1
    # 하 우 상 좌
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # print(q)

    while len(q) != 0:
        node = q.popleft()

        for i in range(4):
            if dx[i]+node[0] >= 0 and dx[i]+node[0] < n and dy[i]+node[1] >= 0 and dy[i]+node[1] < m:  # 미로 내부
                x = dx[i]+node[0]
                y = dy[i]+node[1]
                if graph[x][y] == 1:  # 방문한적 없음
                    # print('방문가능:', x, y)
                    q.append((x, y))
                    graph[x][y] = graph[node[0]][node[1]]-1  # 방문 체크
        # print(node)
    return -1*graph[n-1][m-1]


print(bfs((0, 0), maze, (n-1, m-1)))
