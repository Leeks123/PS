from collections import Counter

n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

def avg(data):
    return sum(data)/n

def mid(data):
    data.sort()
    return data[len(data)//2]

def freq(data):
    counter = Counter(data)
    d = dict(counter)
    l = sorted(d.items(),key=(lambda x: x[1]),reverse=True)
    freqValue = l[0][1]
    filtered = []
    for i in l:
        if i[1]==freqValue:
            filtered.append(i)
        else:
            break
    filtered.sort()
    return filtered[1][0] if not len(filtered)==1 else filtered[0][0]

def ran(data):
    maxNum = max(data)
    minNum = min(data)
    return maxNum-minNum

print(avg(data))
print(mid(data))
print(freq(data))
print(ran(data))