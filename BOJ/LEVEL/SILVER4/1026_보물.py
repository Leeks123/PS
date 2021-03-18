n = int(input())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

argArr = []
rearrangeArr = [0]*n

for i in range(n):
    argArr.append((i, arrB[i]))

argArr.sort(key=lambda x: x[1])
arrA.sort(reverse=True)

for i in range(n):
    rearrangeArr[argArr[i][0]] = arrA[i]

result = 0
for i in range(n):
    result += rearrangeArr[i]*arrB[i]

print(result)
