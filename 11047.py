N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)

count = 0
remainder = K
for a in A:
    if remainder >= a:
        quot, remainder = divmod(remainder, a)
        count += quot
    if remainder == 0:
        break

print(count)