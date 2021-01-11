from collections import Counter

n = int(input())
nArr = list(map(int, input().split()))

m = int(input())
mArr = list(map(int, input().split()))

counter = Counter(nArr)

for i in mArr:
    print(counter[i], end=" ")
