a, b = map(int, input().split())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

ptrA = 0
ptrB = 0

arr = []

while True:
    if ptrA == len(arrA) and ptrB == len(arrB):
        break
    if ptrA == len(arrA):
        arr += arrB[ptrB:]
        break
    if ptrB == len(arrB):
        arr += arrA[ptrA:]
        break

    if arrA[ptrA] > arrB[ptrB]:
        arr.append(arrB[ptrB])
        ptrB += 1
    else:
        arr.append(arrA[ptrA])
        ptrA += 1

for a in arr:
    print(a, end=' ')
