n = int(input())

arrA = list(map(int, input().split()))
arrB = sorted(arrA)
p = [-1 for _ in range(n)]

# print('A: ', arrA)
# print('B: ', arrB)

for i in range(len(arrA)):
    tmp = arrB.index(arrA[i])
    p[i] = tmp
    arrB[tmp] = -1

for i in p:
    print(i, end=' ')
