N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0]*3 for _ in range(N)]
dp[0] = arr[0]

for i in range(1, N):
    # R
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    # G
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    # B
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]


print(min(dp[N-1]))