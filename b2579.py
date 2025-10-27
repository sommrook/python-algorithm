"""
점화식: f(n) = max(f(n-2)+stairs[n], f(n-3)+stairs[n-1]+stairs[n])
"""

import sys

N = int(input())

stairs = [int(input()) if i != 0 else 0 for i in range(N+1)]
result = [0] * (N+1)

if N == 1:
    print(stairs[1])
    sys.exit()
elif N == 2:
    print(stairs[1] + stairs[2])
    sys.exit()
elif N == 0:
    print(0)
    sys.exit()
elif N == 3:
    print(max(stairs[1]+stairs[3], stairs[2]+stairs[3]))
    sys.exit()
else:
    result[1], result[2], result[3] = stairs[1], stairs[1]+stairs[2], max(stairs[1]+stairs[3], stairs[2]+stairs[3])
    for i in range(4, N+1):
        result[i] = max(result[i-2]+stairs[i], result[i-3]+stairs[i-1]+stairs[i])
    print(result[N])