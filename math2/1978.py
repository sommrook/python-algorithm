N = int(input())
arr = list(map(int, input().split()))

count = 0
for i in arr:
    temp = 0
    for j in range(1, i+1):
        if i % j == 0:
            temp += 1
    if temp == 2:
        count += 1

print(count)