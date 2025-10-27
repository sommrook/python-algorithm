N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(0, N):
    for j in range(0, i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)
print(max_dp)
arr = []

for i in range(N-1, -1, -1):
    if dp[i] == max_dp:
        arr.append(A[i])
        max_dp -= 1

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=' ')