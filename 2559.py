import sys

input = sys.stdin.readline

N, K = map(int, input().split())

temperature = list(map(int, input().split()))

max_temp = sum(temperature[0:K])
before_sum = max_temp
for i in range(1, len(temperature)-K+1):
    current_sum = before_sum - temperature[i-1] + temperature[i+K-1]
    max_temp = max(max_temp, current_sum)
    before_sum = current_sum

print(max_temp)