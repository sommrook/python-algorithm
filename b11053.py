N = int(input())
numbers = list(map(int, input().split()))

dp = [1] * N

for i in range(0, N):
    for j in range(0, i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))
