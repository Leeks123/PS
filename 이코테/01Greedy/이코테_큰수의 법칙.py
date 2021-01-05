n, m, k = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
sum = 0
for i in range(m):
    if i%(k+1) == k:
        sum+=arr[-2]
    else:
        sum+=arr[-1]

print(sum)


