# 옆으로만 가는 케이스 빠짐
n, m = map(int, input().split())

move1 = 0

x = 0
y = 0

#     상  하 상좌 하좌
dx = [1, 1, 2,  2]
dy = [-2, 2, -1, 1]

blocked = False

while True:
    # print(x, y, move)
    if move1 == 3:
        if x+dx[2] < m and y+dy[2] < n and x+dx[2] >= 0 and y+dy[2] >= 0:  # 상좌 가능
            if x+dx[2]+dx[3] < m and y+dy[2]+dy[3] < n and x+dx[2]+dx[3] >= 0 and y+dy[2]+dy[3] >= 0:  # 하좌 가능
                x += dx[2]+dx[3]
                y += dy[2]+dy[3]
                move1 += 2
            else:
                break
        else:
            break
    if move1 == 5:
        move1 += m - 8
        break
    for i in range(4):
        if x+dx[i] < m and y+dy[i] < n and x+dx[i] >= 0 and y+dy[i] >= 0:
            x += dx[i]
            y += dy[i]
            move1 += 1
            break
        if i == 3:
            blocked = True
    if blocked:
        break
print(move+1)
