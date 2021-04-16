import re


def countTarget(text, target):
    # print(re.findall(target, text))
    return len(re.findall(target, text))


for _ in range(10):
    n = int(input())
    target = input()
    text = input()
    answer = countTarget(text, target)
    print("#"+str(n), answer)
