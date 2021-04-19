n = int(input())

moves = list(input().split())

#     L R U D
di = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1),
}
current = [0, 0]
for move in moves:
    if current[0]+di[move][0] < 0 or current[0]+di[move][0] >= n or current[1]+di[move][1] < 0 or current[1]+di[move][1] >= n:
        continue
    else:
        current[0] += di[move][0]
        current[1] += di[move][1]

print(current[1]+1, current[0]+1)
