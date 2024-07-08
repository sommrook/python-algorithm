N, X = map(int, input().split())
arr = list(map(int, input().split()))

for n in arr:
    if n < X:
        print(n, end=' ')