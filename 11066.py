import sys
input = sys.stdin.readline

T = int(input())

def get_min_cost(arr):
    n = len(files)
    dp = [[0] * n for _ in range(n)]

    files_sum = [0] * (n+1)
    for i in range(1, n+1):
        files_sum[i] = files_sum[i-1] + arr[i-1]

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + files_sum[j + 1] - files_sum[i]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    print(get_min_cost(files))

