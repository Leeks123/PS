n = int(input())

data = []
for _ in range(n):
    w,h = map(int,input().split())
    data.append((w,h))

def compare(me,another):
    if me[0]<another[0] and me[1]<another[1]:
        return 1
    return 0

rank = [1 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        rank[i] += compare(data[i],data[j])

for i in rank:
    print(i,end=' ')