N, K = map(int, input().split())

arr = []
bag = []

for _ in range(N):
    M, V = map(int, input().split())
    arr.append([M, V])

for _ in range(K):
    C = int(input())
    bag.append(C)