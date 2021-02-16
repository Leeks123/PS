n = int(input())

arr = [0, 1, 1]

for i in range(3, n+2):
    arr.append(arr[i-1]+arr[i-2])

print(2*(arr[n]+arr[n+1]))
