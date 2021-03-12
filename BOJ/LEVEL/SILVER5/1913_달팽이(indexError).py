n = int(input())
findThing = int(input())

board = [[0]*n for _ in range(n)]
pos = []


def fillSnail(n):
    global board
    global pos
    num = n*n
    #     하 좌  상   우
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x, y = 0, 0
    board[x][y] = num
    i = 0
    while True:
        if x+dx[i] < n and y+dy[i] < n and x+dx[i] >= 0 and y+dy[i] >= 0 and board[x+dx[i]][y+dy[i]] == 0:  # 갈 수 있음
            x = x+dx[i]
            y = y+dy[i]
            board[x][y] = num-1
            num -= 1
        else:
            i = (i+1) % 4
        # print(x, y, num)
        if num == findThing:
            pos = [x, y]
        if num == 1:
            break


fillSnail(n)

for i in range(len(board)):
    for j in range(len(board)):
        print(board[i][j], end=' ')
    print()

print(pos[0]+1, pos[1]+1)
