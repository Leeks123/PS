s = input()

currentPos = [ord(s[0])-97, int(s[1])-1]

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

cnt = 0

for i in range(8):
    nx = currentPos[1]+dx[i]
    ny = currentPos[0]+dy[i]
    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
        continue
    else:
        cnt += 1

print(cnt)
