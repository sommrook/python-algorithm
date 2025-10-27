# K: 버틸 수 있는 무게
N, K = map(int, input().split())

W = []
V = []
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# 1 -> 0
for n in range(1, N+1):
    for w in range(1, K+1):
        dp[n][w] = dp[n-1][w]
        if w-W[n-1] >= 0:
            dp[n][w] = max(dp[n][w], dp[n-1][w-W[n-1]] + V[n-1])

print(dp[N][K])