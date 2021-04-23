from collections import deque


def bfs(graph, x, y):
    # print(graph, x, y)
    #    동,동남,남,남서,서,서북,북,북동
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1,  0, 1]

    q = deque([(x, y)])

    if graph[x][y] == 0 or graph[x][y] == -1:
        return 0

    while q:
        v = q.popleft()
        # print(v, end=' ')
        for i in range(8):
            nx = v[0]+dx[i]
            ny = v[1]+dy[i]

            if nx >= 0 and nx < len(graph) and ny >= 0 and ny < len(graph[0]):
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = -1
    return 1


def landCounter(board, w, h):
    cnt = 0
    for i in range(h):
        for j in range(w):
            cnt += bfs(board, i, j)
    return cnt


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))

    print(landCounter(board, w, h))
