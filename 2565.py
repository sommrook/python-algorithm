N = int(input())
telephone_pole = [list(map(int, input().split())) for _ in range(N)]
telephone_pole.sort(key=lambda x: x[0])

dp = [0] * N

for i in range(0, N):
    max_count = 1
    for j in range(0, i):
        if telephone_pole[j][1] < telephone_pole[i][1]:
            max_count = max(dp[j] + 1, max_count)
    dp[i] = max_count

print(N-max(dp))