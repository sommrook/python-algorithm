N, M = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for i in range(0, N):
    for j in range(0, M):
        dp[i][j] = miro[i][j]
        if i-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + miro[i][j])
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + miro[i][j])
        if i-1 >= 0 and j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + miro[i][j])

print(dp[N-1][M-1])
