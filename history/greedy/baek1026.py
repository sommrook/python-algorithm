N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

cnt = 0
for n in range(N):
    cnt += A[n] * B[n]

print(cnt)