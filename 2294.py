n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

INF = 10001
dp = [[INF for _ in range(k+1)] for _ in range(n)]
dp[0][0] = 0  # 0원은 0개 동전

# 첫 번째 동전만 사용할 때
for j in range(1, k+1):
    if j % coins[0] == 0:
        dp[0][j] = j // coins[0]

# 나머지 동전들 사용
for i in range(1, n):
    for j in range(k+1):
        dp[i][j] = dp[i-1][j]
        if j >= coins[i]:
            dp[i][j] = min(dp[i][j], dp[i][j - coins[i]] + 1)

print(dp[n-1][k] if dp[n-1][k] != INF else -1)
