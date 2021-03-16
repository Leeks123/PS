import sys

n, m = map(int, input().split())

DNAs = []
answer = ''
hamDist = 0
#             A C G T
newclCount = [['A', 0], ['C', 0], ['G', 0], ['T', 0]]
for _ in range(n):
    DNAs.append(sys.stdin.readline().rstrip())

for i in range(m):
    for j in range(n):
        if DNAs[j][i] == 'A':
            newclCount[0][1] += 1
        elif DNAs[j][i] == 'C':
            newclCount[1][1] += 1
        elif DNAs[j][i] == 'G':
            newclCount[2][1] += 1
        elif DNAs[j][i] == 'T':
            newclCount[3][1] += 1
    # print(newclCount)
    max = 0
    for c in range(1, 4):
        if newclCount[c][1] > newclCount[max][1]:
            max = c
    # print(newclCount[max][1])
    hamDist += n-newclCount[max][1]
    for c in range(4):
        newclCount[c][1] = 0
    answer += newclCount[max][0]


print(answer)
print(hamDist)
