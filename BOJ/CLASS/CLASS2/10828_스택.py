from sys import stdin

n = int(input())
st = []

for i in range(n):
    s = stdin.readline().split()
    if s[0] == "push":
        st.append(int(s[1]))
    elif s[0] == "pop":
        print(st.pop() if len(st) != 0 else -1)
    elif s[0] == "size":
        print(len(st))
    elif s[0] == "empty":
        print(1 if len(st) == 0 else 0)
    elif s[0] == "top":
        print(st[-1] if len(st) != 0 else -1)
