import math
import sys

N = int(sys.stdin.readline())

dp = [i for i in range(N + 1)]

dp[1] = 1

for i in range(2, N+1):
    for j in range(1, int(math.sqrt(i) + 1)):
        if dp[i] > (dp[i - j * j] + 1):
            dp[i] = dp[i - j * j] + 1

print(dp[N])