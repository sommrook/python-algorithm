N = int(input())

dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])


print(dp[N])

res = [N]
now = N
count = dp[N] - 1

for i in range(N, 0, -1):
    if i+1 == now or i*2 == now or i*3 == now:
        if dp[i] == count:
            now = i
            res.append(i)
            count -= 1

print(*res)