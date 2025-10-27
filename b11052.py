N = int(input())
prices = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for n in range(1, N + 1):
    temp = []
    for p in range(1, N+1):
        if n >= p:
            temp.append(dp[n-p] + prices[p])
    dp[n] = max(temp)

print(dp[N])
