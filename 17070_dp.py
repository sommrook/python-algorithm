N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

"""
0: width
1: height
2: diagonal
"""

dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

dp[0][0][1] = 1
for i in range(2, N):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]


for i in range(1, N):
    for j in range(1, N):
        # 대각선
        if graph[i][j] == 0 and graph[i][j-1] == 0 and graph[i-1][j] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        if graph[i][j] == 0:
            # 가로: 가로 + 대각선
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            # 세로: 세로 + 대각선
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]


print(dp[0][N-1][N-1]+dp[1][N-1][N-1]+dp[2][N-1][N-1])
