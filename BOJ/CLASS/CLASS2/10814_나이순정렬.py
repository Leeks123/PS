n = int(input())

arr = []

for i in range(n):
    age, name = input().split()
    arr.append((int(age), name))

arr = sorted(arr, key=lambda x: x[0])

for x in arr:
    print(x[0], x[1])
