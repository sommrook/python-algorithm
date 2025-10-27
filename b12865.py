from collections import deque

# N: 갯수
# K: 최대 weight
N, K = map(int, input().split())

arr = []
# 0: weight
# 1: value
for _ in range(N):
    arr.append(list(map(int, input().split())))

