n = int(input())
pList = list(map(int, input().split()))

pList.sort()
accList = []
for i in range(len(pList)):
    if i == 0:
        accList.append(pList[i])
    else:
        accList.append(accList[i-1]+pList[i])

print(sum(accList))
