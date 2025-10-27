n = int(input())

dp = [0] * 10001
grape = [0]
for _ in range(n):
    grape.append(int(input()))

if n == 1:
    print(grape[1])
elif n == 2:
    print(grape[1]+grape[2])
else:
    dp[1] = grape[1]
    dp[2] = grape[1]+grape[2]

    for i in range(3, len(grape)):
        dp[i] = max(dp[i-1], dp[i-2]+grape[i], dp[i-3]+grape[i-1]+grape[i])
    print(max(dp))