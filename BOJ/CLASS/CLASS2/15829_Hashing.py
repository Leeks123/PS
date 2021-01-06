l = int(input())
s = input()

arr = []
for c in s:
    arr.append(ord(c)-96)

r = 31
M = 1234567891

sum = 0
for i in range(len(arr)):
    sum+=arr[i]*(r**i)

H = sum % M

print(H)