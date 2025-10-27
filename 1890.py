n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        val = graph[i][j]
        if val == 0 or dp[i][j] == 0:
            continue
        if i+val < n:
            dp[i+val][j] += dp[i][j]
        if j+val < n:
            dp[i][j+val] += dp[i][j]

print(dp[n-1][n-1])