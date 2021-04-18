s = input()

result = int(s[0])
prev = int(s[0])

for i in range(1, len(s)):
    if prev < 2:
        result += int(s[i])
    else:
        if int(s[i]) < 2:
            result += int(s[i])
        else:
            result *= int(s[i])
    prev = int(s[i])

print(result)
