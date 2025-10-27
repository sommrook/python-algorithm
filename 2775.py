T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    dp = [[0 for b in range(n+1)] if a != 0 else [b for b in range(n+1)] for a in range(k+1)]

    for a in range(1, k+1):
        for b in range(1, n+1):
            dp[a][b] = sum(dp[a-1][1:b+1])

    print(dp[k][n])
