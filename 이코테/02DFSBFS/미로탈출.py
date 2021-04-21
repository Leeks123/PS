from collections import deque
n, m = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(n)]


def bfs():
    global board
    q = deque([(0, 0)])
    board[0][0] = 2

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        v = q.popleft()
        for i in range(4):
            nx = v[1]+dx[i]
            ny = v[0]+dy[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if board[ny][nx] == 1:
                    q.append((ny, nx))
                    board[ny][nx] = board[v[0]][v[1]] + 1


bfs()
print(board[-1][-1]-1)
