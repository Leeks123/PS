n, m = map(int, input().split())

catalog = []
for _ in range(m):
    p6, p1 = map(int, input().split())
    catalog.append((p6, p1))

answer = 0
catalog.sort(key=lambda x: x[0])
minPackPrice = catalog[0][0]
catalog.sort(key=lambda x: x[1])
minPiecePrice = catalog[0][1]

answer += (n//6)*minPackPrice if (n//6) * \
    minPackPrice < minPiecePrice*(n//6)*6 else minPiecePrice*(n//6)*6
answer += (n % 6)*minPiecePrice if (n % 6) * \
    minPiecePrice < minPackPrice else minPackPrice

print(answer)
