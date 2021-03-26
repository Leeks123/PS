n = int(input())

level = []
for _ in range(n):
    level.append(int(input()))

level.reverse()

answer = 0

for i in range(1, len(level)):
    if level[i] >= level[i-1]:
        answer += level[i] - level[i-1] + 1
        level[i] = level[i-1]-1

print(answer)
