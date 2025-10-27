N = int(input())
A = list(map(int, input().split()))

dp = [[1] * N for _ in range(2)]

max_count = 1
for i in range(0, N):
    for j in range(0, i):
        if A[i] > A[j]:
            dp[0][i] = max(dp[0][i], dp[0][j] + 1)

    for j in range(N-1, N-i-1, -1):
        if A[N-i-1] > A[j]:
            dp[1][N-i-1] = max(dp[1][N-i-1], dp[1][j] + 1)

for n in range(0, N):
    max_count = max(max_count, dp[0][n] + dp[1][n] - 1)

print(max_count)