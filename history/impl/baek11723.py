import sys

M = int(sys.stdin.readline())
# M = int(input())
# arr = [list(map(str, input().split())) for _ in range(M)]

S = set()
for _ in range(M):
    # sett = input().split()
    sett = sys.stdin.readline().strip().split()
    if sett[0] == "add":
        S.add(int(sett[1]))
    elif sett[0] == "remove":
        S.discard(int(sett[1]))
    elif sett[0] == "check":
        if int(sett[1]) in S:
            print(1)
        else:
            print(0)
    elif sett[0] == "toggle":
        if int(sett[1]) in S:
            S.discard(int(sett[1]))
        else:
            S.add(int(sett[1]))
    elif sett[0] == "all":
        S = set(range(1, 21))
    elif sett[0] == "empty":
        S.clear()
