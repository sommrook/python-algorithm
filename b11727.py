n = int(input())

# f(n) = f(n-1) + 2*f(n-2)
# f(n)/10007 = (f(n-1) + 2*f(n-2))/10007

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + 2*dp[i - 2]) % 10007

print(dp[n])