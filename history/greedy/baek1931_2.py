N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[0]))


start = 0
end = 0
cnt = 0
for con in arr:
    if con[0] >= end:
        cnt += 1
        start = con[0]
        end = con[1]


print(cnt)