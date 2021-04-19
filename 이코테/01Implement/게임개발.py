n, m = map(int, input().split())
cur = [0, 0]
cur[0], cur[1], stare = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

#     북 서 남 동
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

move = 1
cnt = 0
while True:
    # 왼쪽 본다
    stare = (stare+3) % 4
    # 갈 수 있는지 확인한다.
    nx = cur[1] + dx[stare]
    ny = cur[0] + dy[stare]
    print(cur, stare, nx, ny)
    if nx >= 0 or nx < m or ny >= 0 or ny < n:  # 갈 수 있으면 간다
        if board[ny][nx] == 0:
            board[ny][nx] = 2
            cur = [ny, nx]
            move += 1
            print(move, cur)
            cnt = 0
        else:  # 갈 수 없으면
            cnt += 1
            if cnt == 4:
                nx = cur[1] - dx[stare]
                ny = cur[0] - dy[stare]
                if nx >= 0 or nx < m or ny >= 0 or ny < n:
                    if board[ny][nx] == 0:
                        cur = [ny, nx]
                        move += 1
                        cnt = 0
                    else:
                        break

print(move)
