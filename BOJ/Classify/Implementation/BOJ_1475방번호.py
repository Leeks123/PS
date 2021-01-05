n = list(input())
n = list(map(int,n))

count = [0 for _ in range(9)]

for i in n:
    if i==6 or i==9:
        count[6]+=1
    else:
        count[i]+=1

count[6] = count[6]//2 if count[6]%2==0 else count[6]//2+1
# print(count)
print(max(count))
