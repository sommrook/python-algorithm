N = int(input())
withdrawal = list(map(int, input().split()))
withdrawal.sort()

before_sum = 0
total = 0

for p in withdrawal:
    current_sum = before_sum + p
    total += current_sum
    before_sum = current_sum

print(total)