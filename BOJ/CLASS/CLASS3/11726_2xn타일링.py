n = int(input())

arr = [1, 2]

if n < len(arr):
    print(arr[n-1] % 10007)
else:
    for i in range(2, n):
        arr.append(arr[i-1]+arr[i-2])
    print(arr[n-1] % 10007)
