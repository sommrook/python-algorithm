import copy

A = int(input())
numbers = list(map(int, input().split()))
dp = copy.deepcopy(numbers)

for i in range(0, A):
    for j in range(0, i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + numbers[i])

print(max(dp))