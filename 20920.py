import sys

input = sys.stdin.readline

N, M = map(int, input().split())

alpha = {}
for _ in range(N):
    S = input().strip()
    if len(S) >= M:
        if S not in alpha:
            alpha[S] = 1
        else:
            alpha[S] += 1


alpha = sorted(alpha.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for a, c in alpha:
    print(a)