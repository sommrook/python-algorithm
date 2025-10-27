N = int(input())

arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

dp = [[2**31]*N for i in range(N)]
