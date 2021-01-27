s = input().split('-')

addValues = []
for i in s:
    splitByPlus = list(map(int, i.split('+')))
    addValues.append(sum(splitByPlus))

# print(addValues)

ret = addValues[0]
for i in range(1, len(addValues)):
    ret -= addValues[i]

print(ret)
