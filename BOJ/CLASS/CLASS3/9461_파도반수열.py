t = int(input())

WaveArr = [1, 1, 1, 2, 2]


def getWaveArray(n):
    if n <= len(WaveArr):
        return WaveArr[n-1]
    else:
        WaveArr.append(WaveArr[-1]+WaveArr[len(WaveArr)-5])
        return getWaveArray(n)


answer = []
for _ in range(t):
    answer.append(getWaveArray(int(input())))

for i in answer:
    print(i)
