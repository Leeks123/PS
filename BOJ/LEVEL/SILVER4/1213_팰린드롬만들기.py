from collections import Counter

s = input()

cntList = Counter(list(s))
cntList = cntList.most_common()
cntList.sort(key=lambda x: x[0])

oddChar = ''
output = ''

for c in cntList:
    if c[1] % 2 == 1:
        if oddChar != '':
            output = "I'm Sorry Hansoo"
            break
        else:
            oddChar = c[0]
            output += (c[1]//2)*c[0]
    else:
        output += (c[1]//2)*c[0]
    # print(c, oddChar, output)

if output == "I'm Sorry Hansoo":
    print(output)
else:
    print(output+oddChar+output[::-1])
