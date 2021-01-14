from sys import stdin
m = int(stdin.readline())

s = set()

for _ in range(m):
    # cmd = input().split()
    cmd = stdin.readline().split()
    value = 0
    if len(cmd) == 1:
        cmd = cmd[0]
    else:
        value = int(cmd[1])
        cmd = cmd[0]

    if cmd == "add":
        s.add(value)
    elif cmd == "remove":
        if value in s:
            s.remove(value)
    elif cmd == "check":
        if value in s:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        if value in s:
            s.remove(value)
        else:
            s.add(value)
    elif cmd == "all":
        s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                 12, 13, 14, 15, 16, 17, 18, 19, 20])
    else:
        s = set()
