N, K = map(int, input().split())

dp = [[0] * (N+1) if i != 1 else [1] * (N+1) for i in range(K+1)]

for i in range(2, K+1):
    dp[i][0] = 1
    for j in range(1, N+1):
        dp[i][j] = sum(dp[i-1][0:j+1]) % 1000000000

print(dp[K][N] % 1000000000)