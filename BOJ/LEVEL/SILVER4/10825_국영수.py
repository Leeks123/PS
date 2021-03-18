n = int(input())

arr = []

for _ in range(n):
    personData = list(input().split())
    personData[1] = int(personData[1])
    personData[2] = int(personData[2])
    personData[3] = int(personData[3])
    arr.append(personData)

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for a in arr:
    print(a[0])
