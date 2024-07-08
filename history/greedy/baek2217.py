N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort(reverse=True)

max_weight = 0
cnt = 1
for weight in arr:
    if max_weight < weight*cnt:
        max_weight = weight*cnt
    cnt += 1

print(max_weight)