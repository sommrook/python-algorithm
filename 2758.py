import sys
input = sys.stdin.readline

N, K = map(int, input().split())

info = [0] + [list(map(int, input().split())) for _ in range(K)]
dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

for k in range(1, K+1):
    for n in range(1, N+1):
        dp[k][n] = dp[k-1][n]
        if n-info[k][1] >= 0:
            dp[k][n] = max(dp[k][n], dp[k-1][n-info[k][1]] + info[k][0])


print(dp[K][N])