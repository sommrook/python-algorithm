N = int(input())
divide = 10007

dp = [[0] * 10 if i != 1 else [1] * 10 for i in range(N + 1)]

for n in range(2, N + 1):
    for i in range(0, 10):
        dp[n][i] = sum(dp[n-1][0:i+1]) % divide

print(sum(dp[N]) % divide)