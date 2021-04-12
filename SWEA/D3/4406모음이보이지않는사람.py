t = int(input())

for i in range(1, t+1):
    word = input()
    word = word.replace('a', '')
    word = word.replace('i', '')
    word = word.replace('e', '')
    word = word.replace('o', '')
    word = word.replace('u', '')
    print('#'+str(i), word)
