n = int(input())

arr = list(map(int, input().split()))

m = int(input())

search = list(map(int, input().split()))

for i in search:
    if i in arr:
        print(1)
    else:
        print(0)
