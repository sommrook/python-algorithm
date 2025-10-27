N = int(input())

# 길이가 1인 계단 수
# 길이가 2인 계단 수

dp = [[1 if i == 1 else 0] * 10 for i in range(101)]
dp[1][0] = 0
# dp[n] 을 구해야함

for i in range(2, N+1):
    for j in range(0, 10):
        if j == 0:
            dp[i][0] = dp[i-1][1]
        elif j == 9:
            dp[i][9] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)