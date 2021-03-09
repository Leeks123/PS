n = int(input())

paper = [[0]*100 for _ in range(100)]
pos = []
for _ in range(n):
    x, y = map(int, input().split())
    pos.append((x, y))

for p in pos:
    for x in range(p[0]-1, p[0]-1+10):
        for y in range(p[1]-1, p[1]-1+10):
            paper[x][y] = 1

answer = 0
for r in paper:
    answer += r.count(1)

print(answer)
