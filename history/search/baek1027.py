from collections import deque

N = int(input())

building = list(map(int, input().split()))

count = 0
# 기울기? 방정식?
for i, b1 in enumerate(building):
    queue = deque([])
    for b2 in building[i+1:]:
        pass
