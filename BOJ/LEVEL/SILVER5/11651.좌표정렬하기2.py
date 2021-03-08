n = int(input())

pos = []
for _ in range(n):
    x, y = map(int, input().split())
    pos.append((x, y))

pos = sorted(pos, key=lambda x: x[0])
pos = sorted(pos, key=lambda x: x[1])

for p in pos:
    print(p[0], p[1])
