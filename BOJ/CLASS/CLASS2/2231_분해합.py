n = input()


def destructSumGen(n):
    arr = list(map(int, str(n)))
    arr.reverse()
    sum = n
    for i in range(len(arr)):
        sum += arr[i]
    return sum


dSums = [0 for _ in range(1000000)]

i = 0
while True:
    ret = destructSumGen(i)
    if ret > 1000000:
        break
    if dSums[i] == 0:
        dSums[i] = ret
    i += 1

if int(n) in dSums:
    print(dSums.index(int(n)))
else:
    print(0)
