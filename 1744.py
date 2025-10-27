N = int(input())
positive = []
negative = []
ones = 0
zero = False

for _ in range(N):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num == 1:
        ones += 1
    elif num == 0:
        zero = True
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

result = 0

# 양수 짝지어서 곱
for i in range(0, len(positive) - 1, 2):
    result += positive[i] * positive[i+1]
if len(positive) % 2 == 1:
    result += positive[-1]

# 음수 짝지어서 곱
for i in range(0, len(negative) - 1, 2):
    result += negative[i] * negative[i+1]

# 남는 음수 하나는 0이 있으면 없애고, 없으면 더함
if len(negative) % 2 == 1:
    if not zero:
        result += negative[-1]

# 1은 무조건 더하기
result += ones

print(result)
