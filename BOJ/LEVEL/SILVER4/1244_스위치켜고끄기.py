n = int(input())
switches = list(map(int, input().split()))

t = int(input())


def switching(switches, sex, num):
    if sex == 1:
        i = 0
        while num+i < len(switches):
            switches[num+i] = 0 if switches[num+i] == 1 else 1
            i += (num+1)
    else:
        ptrP = num
        ptrN = num
        while True:
            if ptrP - 1 < 0 or ptrN + 1 == len(switches):
                for i in range(ptrP, ptrN+1):
                    switches[i] = 0 if switches[i] == 1 else 1
                break
            ptrP = ptrP-1
            ptrN = ptrN+1
            if switches[ptrP] != switches[ptrN]:
                for i in range(ptrP+1, ptrN):
                    switches[i] = 0 if switches[i] == 1 else 1
                break


for _ in range(t):
    sex, num = map(int, input().split())
    switching(switches, sex, num-1)
    # print(switches)

for i in range(len(switches)):
    print(switches[i], end=' ')
    if (i+1) % 20 == 0:
        print()
