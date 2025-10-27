S = int(input())

count = 0
temp = S
for i in range(1, S+1):
    if temp - i <= i:
        count += 1
        break
    count += 1
    temp -= i

print(count)